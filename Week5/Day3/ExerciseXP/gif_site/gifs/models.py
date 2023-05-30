from django.db import models


class Gif(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()
    uploader_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField('Category', related_name='gifs')

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'
