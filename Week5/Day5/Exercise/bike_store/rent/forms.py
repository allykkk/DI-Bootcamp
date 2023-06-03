import logging

from django import forms
from .models import Rental, Customer, Vehicle


class RentalForm(forms.ModelForm):
    customer_id = forms.IntegerField(label='Customer ID')
    vehicle_id = forms.IntegerField(label='Vehicle ID')

    class Meta:
        model = Rental
        fields = []

    def clean(self):
        cleaned_data = super().clean()
        customer_id = cleaned_data.get('customer_id')
        vehicle_id = cleaned_data.get('vehicle_id')

        if customer_id:
            try:
                customer = Customer.objects.get(id=customer_id)
            except Customer.DoesNotExist:
                raise forms.ValidationError("Invalid customer ID")

        if vehicle_id:
            try:
                vehicle = Vehicle.objects.get(id=vehicle_id)
            except Vehicle.DoesNotExist:
                raise forms.ValidationError("Invalid vehicle ID")

            if Rental.objects.filter(vehicle=vehicle, return_date=None).exists():
                raise forms.ValidationError("The vehicle is currently being rented")

        return cleaned_data


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicle
        exclude=['date_created']

