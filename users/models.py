from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    # User status settings (Choices)
    USER_LEVELS = (
        ('BASIC', 'Bronze'),
        ('REGULAR', 'Silver'),
        ('EXPERT', 'Gold'),
        ('ULTIMATE', 'Platinum')
    )
    
    status = models.CharField(choices=USER_LEVELS, max_length=50)
