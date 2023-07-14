from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profiles/', null=True, blank=True)
    position = models.CharField(max_length=221, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username


def user_post_save(instance, sender, created, *args, **kwargs):
    if created:
        obj = Profile.objects.create(user_post_save, user=instance)
        return obj
    return None


post_save.connect(user_post_save, sender=User)
