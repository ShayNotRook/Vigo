# Generated by Django 5.0.6 on 2024-06-18 13:50

import products.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_alter_giftcard_quantity_giftcardkey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=products.models.game_cover_upload_to),
        ),
    ]
