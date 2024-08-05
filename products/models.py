from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.utils.text import slugify
# Global Variables/Choices
    
PLATFORM_CHOICES = (
    ('Playstation', 'PSN'),
    ('Xbox', 'XBOX/MS'),
    ('Steam', 'STEAM'),
    ('Epic Games', 'EPIC GAMES'),
    ('Itunes', 'ITUNES'),
    
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
    parent = models.ForeignKey('self', related_name='subcategories',on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
            
    
    def get_subcategories(self):
        return self.subcategories.all()
    
    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})
    
    def get_full_path(self):
        subcategories = self.get_subcategories()
        subcategory_urls = []
        for subcategory in subcategories:
            subcategory_urls.append({
                'name': subcategory.name,
                'url': subcategory.get_absolute_url(),
                'subcategories': subcategory.get_full_path(),
                'products': subcategory.get_all_products(),
            })
        return subcategory_urls
    
    def get_all_products(self):
        games = Game.objects.filter(category=self)
        giftcards = GiftCard.objects.filter(category=self)
        gameitems = GameItem.objects.filter(category=self)
        products = list(games) + list(giftcards) + list(gameitems)
        return products
                             

# Models related to Games dataset and metadata.

# Base Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=1000, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    image = models.ImageField(default='/static/default-cover.png')
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.title

def game_cover_upload_to(instance, filename):
    # File will be uploaded to MEDIA_ROOT/game_covers/<filename>
    return f'game_covers/{filename}'
    
class Game(Product):
    category = models.ForeignKey(Category, related_name='games', on_delete=models.CASCADE)
    # name = models.CharField(max_length=255)
    # description = models.TextField(max_length=1500)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=game_cover_upload_to, null=True, blank=True)
    gift_stock = models.IntegerField(name='Steam Gifts', null=True)
    cd_key_stock = models.IntegerField(name='Cd Keys', null=True)
    platform = models.CharField(choices=PLATFORM_CHOICES, default='None', max_length=50)
    # system_requirements = models.OneToOneField(SystemRequirements, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def get_content_type(self):
        return ContentType.objects.get_for_model(self)

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

def gift_cover_upload_to(instance, filename):
    # File will be uploaded to MEDIA_ROOT/gift_covers/<filename>
    return f'gift_covers/{filename}'

class GiftCard(Product):
    category = models.ForeignKey(Category, related_name='giftcards', on_delete=models.CASCADE)
    # name = models.CharField(max_length=255)
    platform = models.CharField(choices=PLATFORM_CHOICES, max_length=255)
    value = models.IntegerField()
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.CharField(choices=REGION_CHOICES, max_length=255)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to=gift_cover_upload_to)
    # price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.platform} - ${self.value} - {self.region}"
    
    def get_content_type(self):
        return ContentType.objects.get_for_model(self)
    
    
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

def item_cover_upload_to(instance, filename):
    # File will be uploaded to MEDIA_ROOT/item_covers/<filename>
    return f'item_covers/{filename}'

class GameItem(Product):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    # name = models.CharField(max_length=100)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    # price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to=item_cover_upload_to)
    platform = models.CharField(choices=PLATFORM_CHOICES, max_length=200, default='Steam')
    
    def __str__(self):
        return f"{self.name} - {self.game}"