import random
from faker import Faker
from django.core.management.base import BaseCommand
from phonebook.models import Person

fake = Faker()


class Command(BaseCommand):
    help = 'Generates fake person records'

    def handle(self, *args, **options):
        for _ in range(50):
            name = fake.name()
            email = fake.email()
            phone_number = fake.phone_number()
            address = fake.address()

            person = Person(name=name, email=email, phone_number=phone_number, address=address)
            person.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully created person: {name}'))
