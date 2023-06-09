from .views import (SignUpView, LoginView, LogOutView,
                    BookingSearchView, AvailableRoomView, MakeBookingView, ConfirmedBookingFormView)
from django.urls import path

app_name = 'visitors'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('search/', BookingSearchView.as_view(), name='search'),
    path('results/', AvailableRoomView.as_view(), name='result'),
    path('booking/', MakeBookingView.as_view(), name='booking'),
    path('submit_check/', ConfirmedBookingFormView.as_view(), name='submit_check'),
]
