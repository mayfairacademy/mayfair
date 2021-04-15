from tinymce import HTMLField
from django.db import models


class Director(models.Model):
    title = models.CharField(max_length=50)
    content = HTMLField()
    image = models.ImageField(upload_to='about/')


    class Meta:
        verbose_name = 'director'
        verbose_name_plural = 'director'

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    content = HTMLField()

    class Meta:
        verbose_name = 'about us'
        verbose_name_plural = 'about us'

    def __str__(self):
        return self.title


class TeamDescription(models.Model): 
    heading = models.CharField(max_length=100)
    summary = HTMLField()

    class Meta:
        verbose_name = 'team description'
        verbose_name_plural = 'team description'

    def __str__(self):
        return self.heading

class Team(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = HTMLField()
    image = models.ImageField(upload_to='about/')


    class Meta:
        verbose_name = 'team'
        verbose_name_plural = 'team'

    def __str__(self):
        return self.name

