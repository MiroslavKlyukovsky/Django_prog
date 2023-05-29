from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Club(models.Model):
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.location


class Day(models.Model):
    name = models.CharField(max_length=15)
    exercise = models.CharField(max_length=20, default="sport")

    def __str__(self):
        return self.name


class Abonement(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    club = models.ManyToManyField(Club)
    days = models.ManyToManyField(Day)

    @property
    def price(self):
        return 15 * self.days.count() * self.club.count()

    def __str__(self):
        days_names = ", ".join([day.name for day in self.days.all()])
        clubs_locations = ", ".join([club.location for club in self.club.all()])
        return f"{clubs_locations} [{days_names}]"


class User(AbstractUser):
    pass
