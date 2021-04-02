import json

from braces.views import LoginRequiredMixin, SuperuserRequiredMixin
from django.contrib import messages
from django.db.models import Q, Count
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
)
from taggit.models import Tag

from .forms import JobListingForm
from .models import JobListing

from rest_framework import viewsets

from .serializers import JobListingSerializer
from .models import JobListing

class JobListingViewSet(viewsets.ModelViewSet):
    queryset = JobListing.objects.all().order_by("title")
    serializer_class = JobListingSerializer

class JobDetail(DetailView):
    """
    Individual job listing view.
    """

    context_object_name = "job"
    model = JobListing
    template_name = "jobs/joblisting_detail.html"

    def get_context_data(self, **kwargs):
        return super(JobDetail, self).get_context_data(
            user_can_edit=(self.object.creator == self.request.user),
            has_flagged="flagged_%s" % self.object.id in self.request.session,
        )

    def get_queryset(self):
        q = Q(status=JobListing.STATUS_ACTIVE)
        if self.request.user.is_authenticated:
            q |= Q(creator=self.request.user)
        return self.model.objects.filter(q).order_by("-created")


class JobList(ListView):
    """
    List of all published jobs.
    """

    context_object_name = "jobs"
    model = JobListing
    template_name = "jobs/joblisting_list.html"

    # our custom fields
    navitem = "all"


class MyJobListings(LoginRequiredMixin, JobList):
    """
    "My listings" page.
    """

    context_object_name = "jobs"
    model = JobListing
    template_name = "jobs/my_joblisting_list.html"

    # our custom fields
    navitem = "mine"

    def get_queryset(self):
        return self.request.user.job_listings.all()


class JobEditMixin(object):
    """
    Common helper for job create/edit.

    Provides:
        * success messages
        * redirect to the job detail on success
    """

    form_class = JobListingForm
    model = JobListing

    def get_context_data(self, **kwargs):
        context = super(JobEditMixin, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context["json_tags"] = json.dumps([t.name for t in tags])
        return context

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        return super(JobEditMixin, self).form_valid(form)

    def get_success_url(self):
        return reverse("job_detail", args=(self.object.id,))


class JobCreate(LoginRequiredMixin, JobEditMixin, CreateView):
    """
    Create a new job listing.
    """

    template_name = "jobs/edit.html"

    # our custom fields
    navitem = "new"
    success_message = "Your job listing has been saved as a draft."

    def get_form_kwargs(self):
        kwargs = super(JobCreate, self).get_form_kwargs()
        kwargs["instance"] = JobListing(
            creator=self.request.user, status=JobListing.STATUS_DRAFT
        )
        return kwargs


class JobEdit(LoginRequiredMixin, JobEditMixin, UpdateView):
    """
    Edit an existing job.

    Naturally only the person who created a job can edit it again.
    """

    template_name = "jobs/edit.html"

    # our custom fields
    success_message = "Your job listing has been updated."

    def get_queryset(self):
        return self.request.user.job_listings.all()


class ChangeJobStatus(object):
    """
    Abstract class to change a job's status; see the concrete implentations below.
    """

    def post(self, request, pk):
        job = get_object_or_404(request.user.job_listings, pk=pk)
        job.status = self.new_status
        job.save()
        messages.add_message(self.request, messages.SUCCESS, self.success_message)
        return redirect("job_detail", job.id)


class PublishJob(LoginRequiredMixin, ChangeJobStatus, View):
    new_status = JobListing.STATUS_ACTIVE
    success_message = "Your job listing has been published."


class ArchiveJob(LoginRequiredMixin, ChangeJobStatus, View):
    new_status = JobListing.STATUS_ARCHIVED
    success_message = "Your job listing has been archived and is no longer public."


class Login(TemplateView):
    template_name = "login.html"

    # our custom fields
    navitem = "login"


class FlagJob(View):
    """
    Flag a job as spam.

    Has some basic protection against overposting, but for the most part we'll
    just assume that people are good citizens and let flags through.
    """

    def post(self, request, pk):
        jobs = JobListing.objects.filter(status=JobListing.STATUS_ACTIVE)
        job = get_object_or_404(jobs, pk=pk)

        # Flag the job, but only if we've not already recorded a flag from this session.
        if "flagged_%s" % pk not in request.session:
            job.flags.create()

        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Thanks for helping to keep our site spam-free! An adminstrator will review this posting shortly.",
        )
        request.session["flagged_%s" % pk] = True

        return redirect("job_detail", job.id)


class ReviewFlags(LoginRequiredMixin, SuperuserRequiredMixin, TemplateView):
    """
    Review and manage flags.
    """

    template_name = "flags.html"

    # our custom fields
    navitem = "flags"

    def get_context_data(self, **kwargs):
        return super(ReviewFlags, self).get_context_data(
            flagged_jobs=JobListing.objects.filter(flags__cleared=False).annotate(
                Count("flags")
            )
        )

    def post(self, request):
        try:
            job = JobListing.objects.get(id=request.POST["job_id"])
            action = request.POST["action"]
        except (KeyError, JobListing.DoesNotExist):
            return redirect("review_flags")

        if action == "kill":
            job.status = JobListing.STATUS_REMOVED
            job.save()
            job.flags.update(cleared=True)
            messages.add_message(self.request, messages.SUCCESS, "'%s' removed." % job)
            # FIXME: ban the user here?

        elif action == "keep":
            job.flags.update(cleared=True)
            messages.add_message(self.request, messages.SUCCESS, "'%s' kept." % job)

        return redirect("review_flags")
