
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class PlanckUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='planckuser_set',  # Unique related_name
        blank=True,
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='planckuser_set',  # Unique related_name
        blank=True,
    )
