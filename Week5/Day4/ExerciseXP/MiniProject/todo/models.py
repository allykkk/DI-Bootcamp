from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name}"


class Todo(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField(blank=True)
    has_been_done = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_completion = models.DateTimeField(null=True, blank=True)
    deadline_date = models.DateTimeField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


