# Generated by Django 3.1.5 on 2021-01-27 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('muslim_school', '0003_auto_20210127_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='welcome',
            name='image',
        ),
    ]