from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_department_admin = models.BooleanField(default=False)


class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    completed = models.BooleanField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
