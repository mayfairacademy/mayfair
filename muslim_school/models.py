from tinymce import HTMLField
from django.db import models

class Sliding(models.Model):
    description = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='home_page/')

    class Meta:
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'

    def __str__(self):
        return self.description


class HeaderOne(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()


    class Meta:
        verbose_name = 'Heading_one'
        verbose_name_plural = 'Heading_one'

    def __str__(self):
        return self.heading 

class HeaderTwo(models.Model):
    heading = models.CharField(max_length=100)
    description = models.TextField()


    class Meta:
        verbose_name = 'Heading_two'
        verbose_name_plural = 'Heading_two'

    def __str__(self):
        return self.heading         


class ApplicationForm(models.Model): 
    description = models.CharField(max_length=200)
    content = HTMLField()
    application_form = models.FileField(upload_to='Application', blank=True)


    class Meta:
        verbose_name = 'Application form'
        verbose_name_plural = 'Application forms'

    def __str__(self):
        return self.description

class Welcome(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    image = models.ImageField(upload_to='Application/', blank=True)
    

    class Meta:
        verbose_name = 'welcome word'
        verbose_name_plural = 'welcome words'

    def __str__(self):
        return self.title


class Achievers(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    image = models.ImageField(upload_to='muslim_school/')


    class Meta:
        verbose_name = 'achievers'
        verbose_name_plural = 'achievers'

    def __str__(self):
        return self.title       


class Staff(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField()
    image = models.ImageField(upload_to='muslim_school/')


    class Meta:
        verbose_name = 'staff'
        verbose_name_plural = 'staff'

    def __str__(self):
        return self.title






