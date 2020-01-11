from django.urls import path

# from . import feeds
from . import views


urlpatterns = [
    path("", views.JobList.as_view(), name="job_list"),
    path("new/", views.JobCreate.as_view(), name="job_create"),
    path("mine/", views.MyListings.as_view(), name="job_list_mine"),
    path("<int:pk>/", views.JobDetail.as_view(), name="job_detail"),
    path("<int:pk>/archive/", views.ArchiveJob.as_view(), name="job_archive"),
    path("<int:pk>/edit/", views.JobEdit.as_view(), name="job_edit"),
    path("<int:pk>/flag/", views.FlagJob.as_view(), name="job_flag"),
    path("<int:pk>/publish/", views.PublishJob.as_view(), name="job_publish"),
    path("flags/", views.ReviewFlags.as_view(), name="review_flags"),
    # path("feed/$", feeds.JobFeed(), name="job_feed"),
    # path("login/$", views.Login.as_view(), name="login"),
    # url(
    #     r"^logout/$",
    #     "django.contrib.auth.views.logout",
    #     {"next_page": "/"},
    #     name="logout",
    # ),
    # url(r"^admin/", include(admin.site.urls)),
    # url(r"", include("social_auth.urls")),
]
