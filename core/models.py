from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Customer', 'Customer'),
        ('SuperAdmin', 'SuperAdmin'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    email = models.CharField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username
