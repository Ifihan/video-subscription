from django.contrib import admin
from .models import Movies,User,Review

# Register your models here.
admin.site.register(Movies)
admin.site.register(User)
admin.site.register(Review)