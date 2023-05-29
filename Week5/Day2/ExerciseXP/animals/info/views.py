from django.shortcuts import render
from .models import Animal,Family

def family_detail(request, family_id):
    family = Family.objects.get(id=family_id)
    animals = Animal.objects.filter(family=family)
    context={'family': family, 'animals': animals}
    return render(request, 'family_detail.html', context)


def animal_detail(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    return render(request, 'animal_detail.html', {'animal': animal})


def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'animal_list.html', {'animals': animals})