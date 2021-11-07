from django.contrib import admin
from .models import Movies,User,Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('movie', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']
    

# Register your models here.
admin.site.register(Movies)
admin.site.register(User)
admin.site.register(Review,ReviewAdmin)