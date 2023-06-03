from django.db import models
from django.utils import timezone


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class VehicleType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class VehicleSize(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, null=True, blank=True, on_delete=models.SET_NULL)
    date_created = models.DateField(auto_now_add=True)
    real_cost = models.DecimalField(max_digits=8, decimal_places=2)
    size = models.ForeignKey(VehicleSize, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.vehicle_type} - {self.size} - id: {self.pk}'

    @property
    def is_rented(self):
        return self.rental_set.filter(return_date__isnull=True).exists()

class Rental(models.Model):
    rental_date = models.DateField(default=timezone.now)
    return_date = models.DateField(blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return f'Rental ID : {self.pk}'


class RentalRate(models.Model):
    daily_rate = models.DecimalField(max_digits=8, decimal_places=2)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(VehicleSize, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.vehicle_type} - {self.vehicle_size}'
