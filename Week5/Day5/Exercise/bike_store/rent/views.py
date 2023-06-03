import logging

from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from rent.models import Rental, Customer, Vehicle
from rent.forms import RentalForm, CustomerForm, VehicleForm


class CustomerListView(View):
    def get(self, request):
        customers = Customer.objects.order_by('first_name', 'last_name')
        return render(request, 'customer_list.html', {'customers': customers})


class CustomerDetailView(View):
    def get(self, request, pk):
        customer = get_object_or_404(Customer, pk=pk)
        rentals = Rental.objects.filter(customer=customer)
        context = {
            'customer': customer,
            'rentals': rentals
        }
        return render(request, 'customer_detail.html', context)


class CustomerCreateView(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'customer_create.html', {'form': form})

    def post(self, request):
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return redirect('customer_list')
        return render(request, 'customer_create.html', {'form': form})


class VehicleListView(View):
    def get(self, request):
        vehicles = Vehicle.objects.all().order_by('vehicle_type', 'size')
        return render(request, 'vehicle_list.html', {'vehicles': vehicles})


class VehicleDetailView(View):
    def get(self, request, pk):
        vehicle = get_object_or_404(Vehicle, pk=pk)
        is_rented = Rental.objects.filter(vehicle=vehicle, return_date__isnull=True).exists()
        context = {
            'vehicle': vehicle,
            'is_rented': is_rented
        }
        return render(request, 'vehicle_detail.html', context)


class VehicleCreateView(View):
    def get(self, request):
        form = VehicleForm()
        return render(request, 'vehicle_create.html', {'form': form})

    def post(self, request):
        form = VehicleForm(request.POST)
        if form.is_valid():
            vehicle = form.save()
            return redirect('vehicle_list')
        return render(request, 'vehicle_create.html', {'form': form})


class RentalCreateView(View):
    def get(self, request):
        form = RentalForm()
        return render(request, 'rental_create.html', {'form': form})

    def post(self, request):
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            customer_id = form.cleaned_data.get('customer_id')
            vehicle_id = form.cleaned_data.get('vehicle_id')
            rental.customer = Customer.objects.get(id=customer_id)
            rental.vehicle = Vehicle.objects.get(id=vehicle_id)
            rental.save()
            return redirect('rental_list')
        return render(request, 'rental_create.html', {'form': form})


class RentalListView(View):
    def get(self, request):
        # rentals=Rental.objects.order_by('-return_date', 'rental_date')
        returned_rentals = Rental.objects.filter(return_date__isnull=False).order_by('rental_date')
        unreturned_rentals = Rental.objects.filter(return_date__isnull=True).order_by('rental_date')
        context = {
            'returned_rentals': returned_rentals,
            'unreturned_rentals': unreturned_rentals,
        }
        return render(request, 'rental_list.html', context)


class RentalDetailView(View):
    def get(self, request, pk):
        rental = get_object_or_404(Rental, pk=pk)
        return render(request, 'rental_detail.html', {'rental': rental})
