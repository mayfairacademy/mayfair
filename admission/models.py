from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Admission(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = HTMLField(max_length=2000, blank=True, null=True)
    image = models.ImageField(upload_to='admission/', blank=True, null=True)


    class Meta:
        verbose_name = 'admission'
        verbose_name_plural = 'admission'

    def __str__(self):
        return self.title


class Fees(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = HTMLField(max_length=2000, blank=True, null=True)
    image = models.ImageField(upload_to='Fees/', blank=True, null=True)


    class Meta:
        verbose_name = 'Fees'
        verbose_name_plural = 'Fees'

    def __str__(self):
        return self.title

class Uniform(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = HTMLField(max_length=2000, blank=True, null=True)
    image = models.ImageField(upload_to='uniform/', blank=True, null=True)


    class Meta:
        verbose_name = 'uniform'
        verbose_name_plural = 'uniform'

    def __str__(self):
        return self.title



