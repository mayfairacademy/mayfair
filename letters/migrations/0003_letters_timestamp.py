# Generated by Django 3.1.7 on 2021-04-01 12:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0002_auto_20210401_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='letters',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
