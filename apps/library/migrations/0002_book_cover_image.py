# Generated by Django 4.2.6 on 2023-11-06 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='cover_images'),
        ),
    ]
