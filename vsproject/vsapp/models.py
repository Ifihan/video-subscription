from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils import timezone

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
    detail_text = models.TextField(max_length=500, verbose_name='Detail Text')
    directors = models.CharField(max_length=200,null=True)
    writers = models.CharField(max_length=200,null=True)
    stars  = models.CharField(max_length=200,null=True)

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    def __str__(self):
        return self.name


class Review(models.Model):
    movie = models.ForeignKey(Movies,related_name='reviews',on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    user_name = models.CharField(max_length=100,default="Unknown user")
    comment = models.TextField(max_length=1000)
    rating = models.IntegerField(default=1,validators=[MaxValueValidator(5),MinValueValidator(1)])
    slug = models.SlugField(default='')
    pub_date = models.DateTimeField('date published',default=timezone.now)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("review", kwargs={"slug": Review.slug})
        
