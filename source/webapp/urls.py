from django.urls import path

from webapp.views.announcement import AnnouncementListView, AnnouncementCreateView, AnnouncementUpdateView, \
    AnnouncementDetailView, AnnouncementDeleteView, AnnouncementModeratedListView, AnnouncementModeratedDetailView

app_name = 'webapp'

urlpatterns = [
    path("", AnnouncementListView.as_view(), name="announcemens_list"),
    path("announcemen/create/", AnnouncementCreateView.as_view(), name="announcemen_create"),
    path("announcemen/<int:pk>/update/", AnnouncementUpdateView.as_view(), name="announcemen_update"),
    path("announcemen/<int:pk>/", AnnouncementDetailView.as_view(), name="announcemen_detail"),
    path("announcemen/<int:pk>/moderated/", AnnouncementModeratedDetailView.as_view(), name="announcemen_moder_detail"),
    path("announcemen/<int:pk>/delete/", AnnouncementDeleteView.as_view(), name="announcemen_delete"),
    path("announcemen/moderated/list/", AnnouncementModeratedListView.as_view(), name="announcemen_moder_list")
]