from tinymce import HTMLField
from django.db import models


class HeadingOne(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()


    class Meta:
        verbose_name = 'Heading_one'
        verbose_name_plural = 'Heading_one'

    def __str__(self):
        return self.heading 

class HeadingTwo(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()


    class Meta:
        verbose_name = 'Heading_two'
        verbose_name_plural = 'Heading_two'

    def __str__(self):
        return self.heading         

class HeadingThree(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()


    class Meta:
        verbose_name = 'Heading_three'
        verbose_name_plural = 'Heading_three'

    def __str__(self):
        return self.heading 

class Slider(models.Model):
    description = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='home_page/')
    text_one = HTMLField(max_length=200, blank=True)
    text_two = HTMLField(max_length=200, blank=True)

    class Meta:
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'

    def __str__(self):
        return self.description

class Application(models.Model): 
    description = models.CharField(max_length=100)
    content = HTMLField()
    application_form = models.FileField(upload_to='Application', blank=True)


    class Meta:
        verbose_name = 'Application form'
        verbose_name_plural = 'Application forms'

    def __str__(self):
        return self.description

class WelcomeWords(models.Model):
    title = models.CharField(max_length=50)
    content = HTMLField()
    image = models.ImageField(upload_to='home_page/')

    class Meta:
        verbose_name = 'welcome word'
        verbose_name_plural = 'welcome words'

    def __str__(self):
        return self.title


class MissionVision(models.Model):
    title = models.CharField(max_length=50)
    content = HTMLField()
    image = models.ImageField(upload_to='home_page/', blank=True)


    class Meta:
        verbose_name = 'mission vision'
        verbose_name_plural = 'mission vision'

    def __str__(self):
        return self.title       







