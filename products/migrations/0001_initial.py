# Generated by Django 5.0.6 on 2024-06-11 13:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('PSN', 'Playstation'), ('XBOX/MS', 'Xbox/Microsoft'), ('STEAM', 'Steam'), ('EPIC GAMES', 'Epic Games'), ('ITUNES', 'Itunes')], max_length=255)),
                ('games', models.TextField(max_length=1500)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1500)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='games/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='GiftCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('platform', models.CharField(choices=[('PSN', 'Playstation'), ('XBOX/MS', 'Xbox/Microsoft'), ('STEAM', 'Steam'), ('EPIC GAMES', 'Epic Games'), ('ITUNES', 'Itunes')], max_length=255)),
                ('value', models.IntegerField()),
                ('region', models.CharField(choices=[('USA', 'United States of America'), ('UK', 'United Kingdoms'), ('GR', 'Germany'), ('FR', 'France')], max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
        migrations.CreateModel(
            name='SystemRequirements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_os', models.CharField(max_length=100)),
                ('directx_version', models.CharField(max_length=100)),
                ('cpu', models.CharField(max_length=255)),
                ('ram', models.CharField(max_length=100)),
                ('graphic_card', models.CharField(max_length=255)),
                ('storage', models.CharField(max_length=100)),
                ('game', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.game')),
            ],
        ),
    ]
