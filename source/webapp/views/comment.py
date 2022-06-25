from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView

from webapp.forms import CommentForm
from webapp.models import Comment, Announcement


class CommentCreateView(CreateView):
    model = Comment
    template_name = "../templates/announcement/announcement_detail.html"
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.announcement = get_object_or_404(Announcement, pk=self.kwargs.get("pk"))
        comment.save()
        return redirect("webapp:announcemen_detail", pk=self.kwargs.get("pk"))
