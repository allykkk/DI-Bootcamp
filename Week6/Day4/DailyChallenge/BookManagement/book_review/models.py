from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from django.shortcuts import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    description = models.TextField()
    page_count = models.PositiveIntegerField()
    categories = models.CharField(max_length=255)
    thumbnail_url = models.URLField()
    average_rating = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    review_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={'pk': self.pk})

    def update_rating(self):
        ratings = self.bookreview_set.all()
        self.average_rating = ratings.aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0
        self.review_count = ratings.count()
        self.save()


class BookReview(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)],)
    review_text = models.TextField()


@receiver(post_save, sender=BookReview)
def update_book_rating(sender, instance, **kwargs):
    instance.book.update_rating()
