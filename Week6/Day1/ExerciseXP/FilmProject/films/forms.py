from django import forms
from .models import Film, Director, Review, Producer
from django.forms import formset_factory


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(),
            'release_date': forms.DateInput(attrs={'type': 'date'}),
            'created_in_country': forms.Select(),
            'available_in_countries': forms.SelectMultiple(),
            'category': forms.SelectMultiple(),
            'director': forms.SelectMultiple(),
        }


class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['film', 'review_text', 'rating']
        # widgets = {
        #     'rating': forms.RadioSelect(attrs={'class': 'form-check-input'})
        # }


class ProducerForm(forms.ModelForm):
    class Meta:
        model = Producer
        fields = '__all__'


ProducerFormSet = formset_factory(ProducerForm)
