from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Movies(models.Model):
    mainimage = models.ImageField(upload_to='vsapp/', blank=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    preview_text = models.TextField(max_length=50, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=100, verbose_name='Detail Text')
    price = models.FloatField()

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.name
