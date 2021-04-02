from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework import routers

from . import feeds
from . import views

router = routers.DefaultRouter()
router.register(r'joblistings', views.JobListingViewSet)

urlpatterns = [
    path("", views.JobList.as_view(), name="job_list"),
    path("<int:pk>/", views.JobDetail.as_view(), name="job_detail"),
    path("<int:pk>/archive/", views.ArchiveJob.as_view(), name="job_archive"),
    path("<int:pk>/edit/", views.JobEdit.as_view(), name="job_edit"),
    path("<int:pk>/flag/", views.FlagJob.as_view(), name="job_flag"),
    path("<int:pk>/publish/", views.PublishJob.as_view(), name="job_publish"),
    path("feed/", feeds.JobFeed(), name="job_feed"),
    path("flags/", views.ReviewFlags.as_view(), name="review_flags"),
    path("login/", views.Login.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("mine/", views.MyJobListings.as_view(), name="job_list_mine"),
    path("new/", views.JobCreate.as_view(), name="job_create"),
    path("api-urls/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
