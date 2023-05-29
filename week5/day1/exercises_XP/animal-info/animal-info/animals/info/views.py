from django.shortcuts import render
import json

def family(request, family_id):
    with open('info/animals.json') as file:
        data = json.load(file)
        animals = [animal for animal in data['animals'] if animal['family'] == family_id]
        family_name = next((family['name'] for family in data['families'] if family['id'] == family_id), '')
        context = {'animals': animals, 'family_name': family_name}
    return render(request, 'family.html', context)

def animal(request, animal_id):
    with open('info/animals.json') as file:
        data = json.load(file)
        animal = next((animal for animal in data['animals'] if animal['id'] == animal_id), {})
        context = {'animal': animal}
    return render(request, 'animal.html', context)
