# Generated by Django 5.0.6 on 2024-07-03 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_game_platform_giftcard_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
