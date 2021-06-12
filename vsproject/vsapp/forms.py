from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from .models import Review

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class  Meta:
       model = User
       fields = ('username',)
       field_classes = { 'username':UsernameField }


class ReviewForm(forms.ModelForm):
    CHOICES = (
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
        )

    rating = forms.ChoiceField(
        choices=CHOICES, 
        required=True,
        label='Rate this movie',
        help_text='Choose a rate 1 = Worst and 5 = Best'
    )

    class Meta:
        model = Review
        fields = ['rating', 'comment']
