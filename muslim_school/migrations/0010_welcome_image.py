# Generated by Django 3.0.6 on 2021-03-28 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muslim_school', '0009_auto_20210328_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='welcome',
            name='image',
            field=models.ImageField(blank=True, upload_to='Application/'),
        ),
    ]
