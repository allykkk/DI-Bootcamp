from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Person


def search_form(request):
    return render(request, 'search.html')


def find_by_phone(request):
    if 'phone_number' in request.GET:
        phone_number = request.GET['phone_number']
        person = get_object_or_404(Person, phone_number=phone_number)
        return render(request, 'find_person.html', {'person': person})
    return render(request, 'search.html')

def find_by_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
        person = get_object_or_404(Person, name=name)
        return render(request, 'find_person.html', {'person': person})
    return render(request, 'search.html')