import json
from info.models import Family,Animal

def import_data():
    with open('data.json') as f:
        data = json.load(f)

        # Import families
        families = data['families']
        for family_data in families:
            family = Family.objects.create(id=family_data['id'], name=family_data['name'])
            family.save()

        # Import animals
        animals = data['animals']
        for animal_data in animals:
            family_id = animal_data['family']
            family = Family.objects.get(id=family_id)

            animal = Animal.objects.create(
                id=animal_data['id'],
                name=animal_data['name'],
                legs=animal_data['legs'],
                weight=animal_data['weight'],
                height=animal_data['height'],
                speed=animal_data['speed'],
                family=family
            )
            animal.save()

if __name__ == '__main__':
    import_data()