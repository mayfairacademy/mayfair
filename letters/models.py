from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Letters(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    content = HTMLField(max_length=2000, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='admission/', blank=True, null=True)
    news_letter = models.FileField(upload_to='letters/', blank=True)


    class Meta:
        verbose_name = 'admission'
        verbose_name_plural = 'admission'

    def __str__(self):
        return self.title

