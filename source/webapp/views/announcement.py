import datetime

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from webapp.forms import AnnouncementCreateForm, SearchForm
from webapp.models import Announcement


class AnnouncementListView(ListView):
    model = Announcement
    template_name = "../templates/announcement/announcement_list.html"
    context_object_name = "announcements"
    paginate_by = 9
    paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        self.form = self.get_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset().filter(status="accepted", is_delete=False).order_by("-publicated_at")
        if self.search_value:
            print(self.search_value)
            query = Q(title__icontains=self.search_value) | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = SearchForm()
        if self.search_value:
            context['form'] = SearchForm(initial={"search": self.search_value})
            context['search'] = self.search_value
        return context

    def get_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data.get("search")



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
