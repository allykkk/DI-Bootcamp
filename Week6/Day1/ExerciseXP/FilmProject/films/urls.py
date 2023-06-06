from .views import HomePageView, FilmCreateView, DirectorCreateView, \
    ReviewCreateView, FilmDeleteView, FavouriteFilmView, FilmDetailView
from django.urls import path

app_name = 'films'

urlpatterns = [
    path('homepage/', HomePageView.as_view(), name='homepage'),
    path('addFilm/', FilmCreateView.as_view(), name='addFilm'),
    path('addDirector/', DirectorCreateView.as_view(), name='addDirector'),
    path('addReview/', ReviewCreateView.as_view(), name='addReview'),
    path('deleteFilm/<int:pk>/', FilmDeleteView.as_view(), name="deleteFilm"),
    path('favoriteFilm/<int:film_id>/', FavouriteFilmView.as_view(), name='favoriteFilm'),
    path('filmDetail/<int:pk>/', FilmDetailView.as_view(), name='filmDetail'),
]
