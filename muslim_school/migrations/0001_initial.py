# Generated by Django 3.1.5 on 2021-01-26 13:06

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField()),
                ('image', models.ImageField(upload_to='muslim_school/')),
            ],
            options={
                'verbose_name': 'achievers',
                'verbose_name_plural': 'achievers',
            },
        ),
        migrations.CreateModel(
            name='ApplicationForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField()),
                ('application_form', models.FileField(blank=True, upload_to='Application')),
            ],
            options={
                'verbose_name': 'Application form',
                'verbose_name_plural': 'Application forms',
            },
        ),
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField()),
                ('image', models.ImageField(upload_to='muslim_school/')),
            ],
            options={
                'verbose_name': 'calender',
                'verbose_name_plural': 'calender',
            },
        ),
        migrations.CreateModel(
            name='HeaderOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='muslim_school/')),
            ],
            options={
                'verbose_name': 'Heading_one',
                'verbose_name_plural': 'Heading_one',
            },
        ),
        migrations.CreateModel(
            name='HeaderThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='muslim_school/')),
            ],
            options={
                'verbose_name': 'Heading_three',
                'verbose_name_plural': 'Heading_three',
            },
        ),
        migrations.CreateModel(
            name='HeaderTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='muslim_school/')),
            ],
            options={
                'verbose_name': 'Heading_two',
                'verbose_name_plural': 'Heading_two',
            },
        ),
        migrations.CreateModel(
            name='Sliding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(upload_to='home_page/')),
            ],
            options={
                'verbose_name': 'slider',
                'verbose_name_plural': 'sliders',
            },
        ),
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', tinymce.models.HTMLField()),
                ('image', models.ImageField(upload_to='muslim_school/')),
            ],
            options={
                'verbose_name': 'welcome word',
                'verbose_name_plural': 'welcome words',
            },
        ),
    ]
