# Generated by Django 3.1.5 on 2021-01-13 07:17

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0007_auto_20210110_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='latestprojects',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='missionvision',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='welcomewords',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
