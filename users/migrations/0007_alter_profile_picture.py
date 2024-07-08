# Generated by Django 5.0.6 on 2024-07-08 11:54

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='default-avatar.jpg', upload_to=users.models.user_picture_upload_to),
        ),
    ]
