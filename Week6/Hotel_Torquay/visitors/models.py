from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class RoomType(models.Model):
    capacity = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=5, decimal_places=2)
    room_name = models.CharField(max_length=25)


class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, blank=True, null=True)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    group_size = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    check_in_date = models.DateField()
    check_out_date = models.DateField()
