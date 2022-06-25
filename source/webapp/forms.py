from django import forms

from webapp.models import Announcement


class AnnouncementCreateForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ("title", "description", "category", "image", "price", )