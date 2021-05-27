from django.db import models


# Create your models here.

class page(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    img = models.ImageField(upload_to='field/')

    def __str__(self):
        return self.title


class ImageSlider(models.Model):
    title = models.CharField(max_length=80)
    image = models.ImageField(upload_to='banner')

    def __str__(self):
        return self.title
