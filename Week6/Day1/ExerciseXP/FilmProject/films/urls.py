from .views import HomePageView, FilmCreateView, DirectorCreateView, ReviewCreateView
from django.urls import path

app_name = 'films'

urlpatterns = [
    path('homepage/', HomePageView.as_view(), name='homepage'),
    path('addFilm/', FilmCreateView.as_view(), name='addFilm'),
    path('addDirector/', DirectorCreateView.as_view(), name='addDirector'),
    path('addReview/', ReviewCreateView.as_view(), name='addReview'),

]
