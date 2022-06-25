from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from accounts.form import AuthorRegistrationForm


class AuthorRegisterView(CreateView):
    model = get_user_model()
    template_name = "../templates/accounts/registration.html"
    form_class = AuthorRegistrationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("webapp:announcemens_list")
