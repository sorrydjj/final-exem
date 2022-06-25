from django.contrib import admin

# Register your models here.
from django.contrib.auth import get_user_model

from webapp.models import Announcement, Category

admin.site.register(Announcement)
admin.site.register(Category)
admin.site.register(get_user_model())