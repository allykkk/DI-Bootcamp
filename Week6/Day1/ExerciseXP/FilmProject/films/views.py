from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, View, DetailView
# from django.views.generic.edit import CreateView
from .models import Film, Director, Review
from .forms import FilmForm, DirectorForm, ReviewForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages


class HomePageView(ListView):
    model = Film
    template_name = 'films/homepage.html'
    context_object_name = 'films'


class FilmCreateView(UserPassesTestMixin, CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'films/addFilm.html'
    success_url = reverse_lazy('films:homepage')

    def test_func(self):
        return self.request.user.is_superuser


class FilmDeleteView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Film
    template_name = 'films/confirm_delete.html'
    success_url = reverse_lazy('films:homepage')
    success_message = "Film deleted successfully."

    def test_func(self):
        return self.request.user.is_superuser

    def get_queryset(self):
        return super().get_queryset().filter(pk=self.kwargs['pk'])

    # do not know why it didn't work, but fixed with inherit from SuccessMessageMixin
    # def delete(self, request, *args, **kwargs):
    #     messages.success(self.request, self.success_message)
    #     response = super().delete(request, *args, **kwargs)
    #     return response


class DirectorCreateView(UserPassesTestMixin, CreateView):
    model = Director
    form_class = DirectorForm
    template_name = 'films/addDirector.html'
    success_url = reverse_lazy('films:homepage')


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'films/addReview.html'
    success_url = reverse_lazy('films:homepage')


class FavouriteFilmView(LoginRequiredMixin, View):
    def post(self, request, film_id):
        film = Film.objects.get(pk=film_id)
        user = request.user

        if film in user.favorite_films.all():
            user.favorite_films.remove(film)
            messages.success(request, f"<{film.title}> removed from favorites.")
        else:
            user.favorite_films.add(film)
            messages.success(request, f"<{film.title}> added to favorites.")

        return redirect('films:homepage')


class FilmDetailView(LoginRequiredMixin, DetailView):
    model = Film
    template_name = 'films/filmDetail.html'
