from django.shortcuts import render
from django.views.generic import CreateView, ListView
# from django.views.generic.edit import CreateView
from .models import Film, Director, Review
from .forms import FilmForm, DirectorForm, ReviewForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin


class HomePageView(ListView):
    model = Film
    template_name = 'films/homepage.html'
    context_object_name = 'films'


class FilmCreateView(UserPassesTestMixin,CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'films/addFilm.html'
    success_url = reverse_lazy('films:homepage')

    def test_func(self):
        return self.request.user.is_superuser

class DirectorCreateView(UserPassesTestMixin,CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'films/addDirector.html'
    success_url = reverse_lazy('films:homepage')

    def test_func(self):
        return self.request.user.is_superuser


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'films/addReview.html'
    success_url = reverse_lazy('films:homepage')
