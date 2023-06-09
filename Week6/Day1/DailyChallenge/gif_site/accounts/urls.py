from .views import LoginView,LogoutView,SignupView,ProfileView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('profile/<int:id>', ProfileView.as_view(), name='signup'),
]
