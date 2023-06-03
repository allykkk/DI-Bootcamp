from django.shortcuts import render
from .models import Person

def search_by_phonenumber(request):
    if 'phonenumber' in request.GET:
        phonenumber = request.GET['phonenumber']
        try:
            person = Person.objects.get(phone_number=phonenumber)
            return render(request, 'person_detail.html', {'person': person})
        except Person.DoesNotExist:
            return render(request, 'person_not_found.html')
    return render(request, 'search_phonenumber.html')

def search_by_name(request):
    if 'name' in request.GET:
        name = request.GET['name']
        try:
            person = Person.objects.get(name__icontains=name)
            return render(request, 'person_detail.html', {'person': person})
        except Person.DoesNotExist:
            return render(request, 'person_not_found.html')
    return render(request, 'search_name.html')
