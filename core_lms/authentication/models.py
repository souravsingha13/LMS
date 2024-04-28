from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from .manager import UserManager


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

      
    objects = UserManager()

    def __str__(self):
        return self.email