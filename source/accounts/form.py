from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class AuthorRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ("first_name", "last_name", "username", "phone", "password1", "password2",)
        widgets = {}
        labels = {"first_name": "Имя", "last_name": "Фамилия", "username": "Никнейм", "phone": "Номер телефона",
                  "password1": "Пароль", "password2": "Повторите пароль"}

        def save(self, commit=True):
            user = super(UserCreationForm, self).save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user


class AuthorUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "username", "phone",)
        widgets = {}
        labels = {"first_name": "Имя", "last_name": "Фамилия", "username": "Никнейм", "phone": "Номер телефона", }


