import json
from django.shortcuts import render


def open_json_file():
    with open('data.json') as file:
        data = json.load(file)
        return data


def family_detail(request, family_id):
    data = open_json_file()
    # fetch families part from json file
    families = data['families']
    family_name=next((family['name'] for family in families if family['id'] == int(family_id)), None)
    # get animal name from animals part and store it in a list where family id equals to the given one
    # animals_in_families is a list of dictionaries
    animals_in_families = [animal for animal in data['animals'] if animal['family'] == family_id]

    context = {
        'family_id': family_id,
        'family_name': family_name,
        'animals': animals_in_families
    }

    return render(request, 'family_detail.html', context)


def animal_detail(request, animal_id):
    data = open_json_file()
    # return dictionary that contains info about the selected animal
    animal = next((animal for animal in data['animals'] if animal['id'] == animal_id), None)

    context = {
        'animal': animal
    }
    return render(request, 'animal_detail.html', context)


def animal_list(request):
    data=open_json_file()
    animals =data['animals']
    context={
        'animals':animals
    }
    return render(request, 'animal_list.html', context)