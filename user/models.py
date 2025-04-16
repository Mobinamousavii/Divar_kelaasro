from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    national_id = models.CharField(max_length=11, unique=True)

    def __str__(self):
        return self.username
