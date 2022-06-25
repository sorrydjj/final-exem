from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext as _


class Author(AbstractUser):
    phone = PhoneNumberField(unique=True, region="KG", max_length=15, verbose_name=_('Номер телефона'))

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}"



