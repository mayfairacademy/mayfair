# Generated by Django 3.1.7 on 2021-03-18 06:45

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0010_missionvision_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='text_one',
            field=tinymce.models.HTMLField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='slider',
            name='text_two',
            field=tinymce.models.HTMLField(blank=True, max_length=200),
        ),
    ]
