# Generated by Django 4.1.1 on 2022-12-22 18:36

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0007_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255),
        ),
    ]
