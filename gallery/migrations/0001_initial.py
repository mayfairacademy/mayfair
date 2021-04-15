# Generated by Django 3.1.5 on 2021-01-10 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('image_gallery', models.ImageField(upload_to='gallery/')),
            ],
            options={
                'verbose_name': 'gallery',
                'verbose_name_plural': 'galleries',
            },
        ),
        migrations.CreateModel(
            name='GallerySlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('image_gallery', models.ImageField(upload_to='gallery/')),
            ],
            options={
                'verbose_name': 'gallery_slider',
                'verbose_name_plural': 'gallery_sliders',
            },
        ),
    ]