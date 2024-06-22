from django.db import models
from django.contrib.auth.models import AbstractUser

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
    
    def get_discount(self):
        for group in self.groups.all():
            if group.name.lower() in DISCOUNT_MAP:
                return DISCOUNT_MAP[group.name.lower()]
            
            return 0.00
            
