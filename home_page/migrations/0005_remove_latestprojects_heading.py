# Generated by Django 3.1.5 on 2021-01-10 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0004_auto_20210110_1301'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='latestprojects',
            name='heading',
        ),
    ]