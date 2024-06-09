from django.db import models


# Global Variables/Choices
    
PLATFORM_CHOICES = (
    ('PSN', 'Playstation'),
    ('XBOX/MS', 'Xbox/Microsoft'),
    ('STEAM', 'Steam'),
    ('EPIC GAMES', 'Epic Games'),
    ('ITUNES', 'Itunes')
)

REGION_CHOICES = (
    ('USA', 'United States of America'),
    ('UK', 'United Kingdoms'),
    ('GR', 'Germany'),
    ('FR', 'France'),
)



# Models for Products dataset.

class Category(models.Model):
    title = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.title
    

# Models related to Games dataset and metadata.

class SystemRequirements(models.Model):
    required_os = models.CharField(max_length=100)
    directx_version = models.CharField(max_length=100)
    cpu = models.CharField(max_length=255)
    ram = models.CharField(max_length=100)
    graphics_card = models.CharField(max_length=255)
    storage = models.CharField(max_length=100)
    
class Game(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1500)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='games/')
    system_requirements = models.ForeignKey(SystemRequirements, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    


# Gift Card Metadata.

class GiftCard(models.Model):
    name = models.CharField(max_length=255)
    platform = models.CharField(choices=PLATFORM_CHOICES)
    value = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    region = models.CharField(choices=REGION_CHOICES)
    
    def __str__(self):
        return f"{self.platform} - ${self.value} - {self.region}"
    
    
    
# Account base models

class Account(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    platform = models.CharField(choices=PLATFORM_CHOICES)
    games = models.TextField(max_length=1500)