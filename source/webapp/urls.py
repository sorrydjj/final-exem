from django.urls import path, include

from webapp.views.announcement import AnnouncementListView, AnnouncementCreateView, AnnouncementUpdateView, \
    AnnouncementDetailView, AnnouncementDeleteView, AnnouncementModeratedListView, AnnouncementModeratedDetailView
from webapp.views.api import set_status_accept, set_status_reject
from webapp.views.comment import CommentCreateView

app_name = 'webapp'

api_urlpatterns = [
    path("accept/announcemen/", set_status_accept),
    path("reject/announcemen/", set_status_reject),
]

urlpatterns = [
    path("", AnnouncementListView.as_view(), name="announcemens_list"),
    path("announcemen/create/", AnnouncementCreateView.as_view(), name="announcemen_create"),
    path("announcemen/<int:pk>/update/", AnnouncementUpdateView.as_view(), name="announcemen_update"),
    path("announcemen/<int:pk>/", AnnouncementDetailView.as_view(), name="announcemen_detail"),
    path("announcemen/<int:pk>/moderated/", AnnouncementModeratedDetailView.as_view(), name="announcemen_moder_detail"),
    path("announcemen/<int:pk>/delete/", AnnouncementDeleteView.as_view(), name="announcemen_delete"),
    path("announcemen/moderated/list/", AnnouncementModeratedListView.as_view(), name="announcemen_moder_list"),
    path("comment/add/<int:pk>/", CommentCreateView.as_view(), name="add_comment"),
    path("api/", include(api_urlpatterns))
]