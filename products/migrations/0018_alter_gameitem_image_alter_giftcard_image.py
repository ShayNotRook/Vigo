# Generated by Django 5.0.7 on 2024-07-23 13:49

import products.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_gameitem_image_alter_giftcard_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameitem',
            name='image',
            field=models.ImageField(upload_to=products.models.item_cover_upload_to),
        ),
        migrations.AlterField(
            model_name='giftcard',
            name='image',
            field=models.ImageField(upload_to=products.models.gift_cover_upload_to),
        ),
    ]
