from tinymce import HTMLField
from django.db import models


class Family(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    bio = HTMLField()
    image = models.ImageField(upload_to='family/', blank=True, null=True)


    class Meta:
        verbose_name = 'family'
        verbose_name_plural = 'family'

    def __str__(self):
        return self.name
