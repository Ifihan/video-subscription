from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

class Movies(models.Model):
    mainimage = models.ImageField(upload_to='vsapp/', blank=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    genre = models.CharField(max_length=20,default='genre')
    release_period = models.CharField(max_length=20,default='release period')
    preview_text = models.TextField(max_length=150, verbose_name='Preview Text')
    detail_text = models.TextField(max_length=200, verbose_name='Detail Text')

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.name
