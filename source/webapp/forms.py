from django import forms

from webapp.models import Announcement


class AnnouncementCreateForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ("title", "description", "category", "image", "price", )

class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")