from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class AnnouncementStatusChoices(TextChoices):
    ACCEPTED = "accepted", _("Принято")
    MODERATED = "moderated", _("На модерации")
    REJECTED = "rejected", _("Отклонено")
