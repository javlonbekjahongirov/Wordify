from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=221)
    phone_number = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.full_name
