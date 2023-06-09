from .views import SignupView,LoginView,LogoutView,ProfileView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:user_id>/', ProfileView.as_view(), name='profile'),

]
