import datetime

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from webapp.choice import AnnouncementStatusChoices


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=_("Категория"))

    def __str__(self):
        return self.name


class Announcement(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Заголовок"))
    description = models.CharField(max_length=2000, verbose_name=_("Описание"))
    category = models.ForeignKey("webapp.Category", on_delete=models.CASCADE, related_name="announcement_category")
    image = models.ImageField(upload_to='uploads/', verbose_name=_('Изображение'))
    price = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)], verbose_name=_("Цена"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Дата созждания"))
    update_at = models.DateTimeField(verbose_name=_("Дата редактирования"), null=True, blank=True)
    publicated_at = models.DateTimeField(verbose_name=_("Дата публикации"), null=True, blank=True)
    status = models.CharField(max_length=25, choices=AnnouncementStatusChoices.choices,
                              verbose_name=_("Статус объявления"), default="moderated")
    is_delete = models.BooleanField(default=False, verbose_name=_("Статус удаления"))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="announcement_user", verbose_name=_("Автор"))

    class Meta:
        db_table = 'announcement'
        verbose_name = _('Объявление')
        verbose_name_plural = _('Объявления')

    def set_time_now(self):
        self.update_at = datetime.datetime.now()
        self.save()

