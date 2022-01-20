from django import forms
from django.forms import ModelForm,Textarea
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from .models import Review

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class  Meta:
       model = User
       fields = ('username',)
       field_classes = { 'username':UsernameField }



class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'rating', 'comment']
        widgets = {
            'comment': Textarea(attrs={'cols': 40, 'rows': 15})
        }