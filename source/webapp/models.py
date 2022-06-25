from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from webapp.choice import AnnouncementStatusChoices


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Категория"))


class Announcement(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Заголовок"))
    description = models.CharField(max_length=2000, verbose_name=_("Описание"))
    category = models.ForeignKey("webapp.Category", on_delete=models.CASCADE, related_name="announcement")
    image = models.ImageField(upload_to='uploads/', verbose_name=_('Изображение'))
    price = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)], verbose_name=_("Цена"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата созждания"))
    update_at = models.DateTimeField(verbose_name=_("Дата редактирования"))
    publicated_at = models.DateTimeField(verbose_name=_("Дата публикации"))
    status = models.CharField(max_length=25, choices=AnnouncementStatusChoices.choices,
                              verbose_name=_("Статус объявления"))
    is_delete = models.BooleanField(default=False, verbose_name=_("Статус удаления"))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_("Автор"))
