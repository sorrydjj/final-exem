from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView

from accounts.form import AuthorRegistrationForm, AuthorUpdateForm

User = get_user_model()


class AuthorRegisterView(CreateView):
    model = User
    template_name = "../templates/accounts/registration.html"
    form_class = AuthorRegistrationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("webapp:announcemens_list")


class AuthorProfileView(DetailView):
    model = User
    template_name = "../templates/accounts/profile.html"
    context_object_name = "author"


class AuthorUpdateView(UpdateView):
    model = User
    template_name = "../templates/accounts/profile_update.html"
    form_class = AuthorUpdateForm

    def get_success_url(self):
        return reverse("accounts:profile", kwargs={"pk": self.get_object().pk})