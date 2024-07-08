from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Status groups definers
DISCOUNT_MAP = {
    'bronze': 5.00,
    'silver': 10.00,
    'gold': 15.00,
    'platinum': 20.00
}

class User(AbstractUser):
    # User status settings (Choices)
    # USER_LEVELS = (
    #     ('BASIC', 'Bronze'),
    #     ('REGULAR', 'Silver'),
    #     ('EXPERT', 'Gold'),
    #     ('ULTIMATE', 'Platinum')
    # )
    
    # status = models.ForeignKey(Status, on_delete=models.CASCADE)
    
    # profile_picture = models.ImageField()
    
    def get_discount(self):
        for group in self.groups.all():
            if group.name.lower() in DISCOUNT_MAP:
                return DISCOUNT_MAP[group.name.lower()]
            
            return 0.00


def user_picture_upload_to(instance, filename):
    return f'profile_pictures/{filename}'
   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to=user_picture_upload_to, default='default-avatar.jpg')
    bio = models.TextField(blank=True, null=True, default='<blank>')