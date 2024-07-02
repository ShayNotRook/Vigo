from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Global Variables/Choices
    
PLATFORM_CHOICES = (
    ('PSN', 'Playstation'),
    ('XBOX/MS', 'Xbox/Microsoft'),
    ('STEAM', 'Steam'),
    ('EPIC GAMES', 'Epic Games'),
    ('ITUNES', 'Itunes'),
    
)

REGION_CHOICES = (
    ('USA', 'United States of America'),
    ('UK', 'United Kingdoms'),
    ('GR', 'Germany'),
    ('FR', 'France'),
)


# Offer model
class Offer(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    discount_percentage = models.DecimalField(max_digits=4, decimal_places=2)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    
    @staticmethod
    def calculate_offer_price(offer, product):
        return product.price * (1 - offer.discount_percentage / 100)


# Models for Products dataset.

class Category(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.title
    

# Models related to Games dataset and metadata.

def game_cover_upload_to(instance, filename):
    # File will be uploaded to MEDIA_ROOT/game_covers/<filename>
    return f'game_covers/{filename}'
    
class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1500)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=game_cover_upload_to, null=True, blank=True)
    gift_quantity = models.IntegerField(name='Steam Gifts', null=True)
    cd_key_quantity = models.IntegerField(name='Cd Keys', null=True)
    platform = models.CharField(choices=PLATFORM_CHOICES, default='None', max_length=50)
    # system_requirements = models.OneToOneField(SystemRequirements, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class SystemRequirement(models.Model):
    game = models.OneToOneField(Game, on_delete=models.CASCADE, default=1)
    required_os = models.CharField(max_length=100)
    directx_version = models.CharField(max_length=100)
    cpu = models.CharField(max_length=255)
    ram = models.CharField(max_length=100)
    graphic_card = models.CharField(max_length=255)
    storage = models.CharField(max_length=100)


class ProductKey(models.Model):
    key = models.CharField(max_length=50, unique=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE,
                             related_name='cd_keys')
    issued_date = models.DateField(auto_now_add=True)
    redeemed = models.BooleanField(default=False)
    platform = models.CharField(max_length=100 ,choices=PLATFORM_CHOICES)


# Gift Card Metadata.

class GiftCard(models.Model):
    name = models.CharField(max_length=255)
    platform = models.CharField(choices=PLATFORM_CHOICES, max_length=255)
    value = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.CharField(choices=REGION_CHOICES, max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField()
    
    def __str__(self):
        return f"{self.platform} - ${self.value} - {self.region}"
    
    
    
class GiftcardKey(models.Model):
    key = models.CharField(max_length=50)
    giftcard = models.ForeignKey(GiftCard, on_delete=models.CASCADE, related_name='keys')
    redeemed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.key[:10]
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.giftcard.quantity = self.giftcard.keys.count()
        self.giftcard.save()
    
# Account base models

class Account(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    platform = models.CharField(choices=PLATFORM_CHOICES, max_length=255)
    games = models.TextField(max_length=1500)
    
    
# Items
class GameItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.name} - {self.game}"