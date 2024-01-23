from django.contrib.auth.models import Permission, Group, AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    class Meta:
        db_table = 'neiro_authusers'

    name = models.CharField(max_length=40, blank=True)
    avatar_img = models.ImageField(null=True, blank=True)
    banner_img = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=100, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='users',
        related_query_name='user',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='user_permissions',
        related_query_name='user_permission',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )