from .models import BookReview
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class BookReviewForm(forms.ModelForm):
#     class Meta:
#         model = BookReview
#         fields = "__all__"


class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'password1', 'password2']
