from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


from .managers import CustomUserManager

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True, error_messages={
        'unique': _("A user with that email already exists."),
        'required': _("Email id is required, please enter a valid email address.")})

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username} ({self.email})"
