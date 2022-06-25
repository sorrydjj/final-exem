from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from webapp.forms import AnnouncementCreateForm
from webapp.models import Announcement


class AnnouncementListView(ListView):
    model = Announcement
    template_name = "../templates/announcement/announcement_list.html"
    context_object_name = "announcements"

    def get_queryset(self):
        return super().get_queryset().filter(status="accepted", is_delete=False)


class AnnouncementCreateView(CreateView):
    model = Announcement
    template_name = "../templates/announcement/announcement_create.html"
    form_class = AnnouncementCreateForm


class AnnouncementUpdateView(UpdateView):
    model = Announcement
    template_name = "../templates/announcement/announcement_update.html"
    form_class = AnnouncementCreateForm


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = "../templates/announcement/announcement_detail.html"
    context_object_name = "announcement"


class AnnouncementDeleteView(DeleteView):
    model = Announcement
    template_name = "../templates/announcement/announcement_delete.html"
