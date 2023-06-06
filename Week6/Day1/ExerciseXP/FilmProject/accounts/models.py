from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from films.models import Film

class User(AbstractUser):
    favorite_films = models.ManyToManyField(Film, related_name='users_favorite', blank=True)
    groups = models.ManyToManyField(Group, related_name='accounts_users', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='accounts_users', blank=True)


