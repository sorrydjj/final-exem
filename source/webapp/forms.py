from django import forms

from webapp.models import Announcement, Comment


class AnnouncementCreateForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ("title", "description", "category", "image", "price", )


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, required=False, label="Найти")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment", )
        labels = {"comment": "Комментарий"}