# Generated by Django 5.0.7 on 2024-07-10 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_category_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='giftcard',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]