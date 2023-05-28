from django.shortcuts import render
import json
# Create your views here.

def open_json_file():
    with open('data.json') as file:
        data = json.load(file)
        return data

def people_list(request):
    data=open_json_file()
    sorted_data=sorted(data, key=lambda person: person['age'])
    context={
        'people':sorted_data
    }
    return render(request,'list.html',context)

def person_detail(request,id):
    data=open_json_file()
    person= next((person for person in data if person['id'] == id), None)
    context={
        'person':person
    }
    return render(request, 'detail.html', context)