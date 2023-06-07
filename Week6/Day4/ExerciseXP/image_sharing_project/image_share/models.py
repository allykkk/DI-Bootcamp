from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_count = models.IntegerField(default=0)



class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    description = models.TextField()


@receiver(post_save, sender=Image)
def update_profile(sender, instance, created, **kwargs):
    if created:
        user = instance.user
        profile = Profile.objects.get_or_create(user=user)[0]
        profile.image_count += 1
        profile.save()