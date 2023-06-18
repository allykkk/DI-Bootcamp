from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class RoomType(models.Model):
    capacity = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=5, decimal_places=2)
    room_name = models.CharField(max_length=25)
    description = models.TextField()


class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.room_type.room_name} - {self.room_number}"

    @staticmethod
    def get_free_rooms(check_in_date, check_out_date):
        available_rooms = Room.objects.exclude(booking__check_in_date__range=(check_in_date, check_out_date))
        available_rooms = available_rooms.exclude(booking__check_out_date__range=(check_in_date, check_out_date))
        return available_rooms

    @staticmethod
    def filter_capacity(query_set, group_size):
        return query_set.exclude(room_type__capacity__lt=group_size)

    @staticmethod
    def filter_type(query_set, room_type):
        return query_set.filter(room_type__id=room_type)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    group_size = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)])
    check_in_date = models.DateField()
    check_out_date = models.DateField()


class UserRequest(models.Model):
    # visitors can send requests as well, but if we have user info, we want to link to the user
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='requests')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    # store the time when request is made, so we can deal with the requests in time order for future use
    request_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"
