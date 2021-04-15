# Generated by Django 3.1.5 on 2021-01-28 07:32

from django.db import migrations, models
import embed_video.fields
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='content',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
