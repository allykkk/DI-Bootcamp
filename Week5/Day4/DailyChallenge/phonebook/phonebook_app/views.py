from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Person


def search_view(request):
    if request.method == 'POST':
        search_term = request.POST.get('search_term')
        persons = Person.objects.filter(phone_number=search_term)
        if not persons:
            persons = Person.objects.filter(name__icontains=search_term)
        return redirect('person_search', search_term=search_term)
    return render(request, 'search.html')

def find_person(request, search_term):
    persons = Person.objects.filter(phone_number=search_term) | Person.objects.filter(name__icontains=search_term)
    return render(request, 'find_person.html', {'persons': persons, 'search_term': search_term})