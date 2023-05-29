from django.db import models


class Family(models.Model):
    name=models.CharField(max_length=50,default='')


class Animal(models.Model):
    name = models.CharField(max_length=50)
    legs = models.PositiveIntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    speed = models.FloatField()
    family = models.ForeignKey(Family, on_delete=models.CASCADE)




