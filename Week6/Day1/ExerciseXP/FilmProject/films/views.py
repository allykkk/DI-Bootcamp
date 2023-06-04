from django.shortcuts import render
from django.views.generic import CreateView, ListView
# from django.views.generic.edit import CreateView
from .models import Film, Director,Review
from .forms import FilmForm, DirectorForm,ReviewForm
from django.urls import reverse_lazy



class HomePageView(ListView):
    model = Film
    template_name = 'homepage.html'
    context_object_name = 'films'


class FilmCreateView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'addFilm.html'
    success_url = reverse_lazy('films:homepage')


class DirectorCreateView(CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'addDirector.html'
    success_url = reverse_lazy('films:homepage')


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'addReview.html'
    success_url = reverse_lazy('films:homepage')

