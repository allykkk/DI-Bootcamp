"""
URL configuration for bike_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rent import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rent/customer/', views.CustomerListView.as_view(), name='customer_list'),
    path('rent/customer/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('rent/customer/add/', views.CustomerCreateView.as_view(), name='customer_create'),
    path('rent/vehicle', views.VehicleListView.as_view(), name='vehicle_list'),
    path('rent/vehicle/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle_detail'),
    path('rent/vehicle/add/', views.VehicleCreateView.as_view(), name='vehicle_create'),
    path('rent/rental/', views.RentalListView.as_view(), name='rental_list'),
    path('rent/rental/<int:pk>/', views.RentalDetailView.as_view(), name='rental_detail'),
    path('rent/rental/add/', views.RentalCreateView.as_view(), name='rental_create'),

]
