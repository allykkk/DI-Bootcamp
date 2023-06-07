from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, DeleteView, View, DetailView
from .models import Film, Director, Review
from .forms import FilmForm, DirectorForm, ReviewForm, ProducerFormSet
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.forms import formset_factory


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

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = ProducerFormSet(self.request.POST, prefix='producers')
        else:
            data['formset'] = ProducerFormSet(prefix='producers')
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            for form in formset:
                producer = form.save(commit=False)
                producer.film = self.object
                producer.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


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


class ReviewCreateView(LoginRequiredMixin, CreateView):
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
