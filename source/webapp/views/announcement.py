import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from webapp.forms import AnnouncementCreateForm
from webapp.models import Announcement


class AnnouncementListView(ListView):
    model = Announcement
    template_name = "../templates/announcement/announcement_list.html"
    context_object_name = "announcements"

    def get_queryset(self):
        print(self.request.user.username)
        return super().get_queryset().filter(status="accepted", is_delete=False).order_by("-publicated_at")


class AnnouncementCreateView(LoginRequiredMixin, CreateView):
    model = Announcement
    template_name = "../templates/announcement/announcement_create.html"
    form_class = AnnouncementCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return redirect("webapp:announcemen_detail", pk=form.instance.pk)


class AnnouncementUpdateView(PermissionRequiredMixin, UpdateView):
    model = Announcement
    template_name = "../templates/announcement/announcement_update.html"
    form_class = AnnouncementCreateForm
    permission_required = "webapp.change_announcement"

    def form_valid(self, form):
        form.instance.update_at.set_time_now()
        form.save()
        return redirect("webapp:announcemen_detail", pk=form.instance.pk)

    def has_permission(self):
        return self.request.user == self.get_object().author


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = "../templates/announcement/announcement_detail.html"
    context_object_name = "announcement"


class AnnouncementDeleteView(PermissionRequiredMixin, DeleteView):
    model = Announcement
    template_name = "../templates/announcement/announcement_delete.html"
    permission_required = "webapp.delete_announcement"

    def form_valid(self, form):
        self.object.is_delete = True
        self.object.save()
        return HttpResponseRedirect(self.success_url)

    def get_success_url(self):
        return reverse("webapp:announcemens_list")

    def has_permission(self):
        return self.request.user == self.get_object().author


class AnnouncementModeratedListView(PermissionRequiredMixin, ListView):
    model = Announcement
    template_name = "../templates/announcement/moderated_list.html"
    context_object_name = "announcements"
    permission_required = "webapp.view_announcement"

    def get_queryset(self):
        return super().get_queryset().filter(status="moderated").exclude(is_delete=True).order_by("created_at")


class AnnouncementModeratedDetailView(PermissionRequiredMixin, DetailView):
    model = Announcement
    template_name = "../templates/announcement/moderated_detail.html"
    context_object_name = "announcement"
    permission_required = "webapp.view_announcement"
