from django.core.management.base import BaseCommand
from faker import Faker
from films.models import Director

fake = Faker()

class Command(BaseCommand):
    help = 'Creates fake directors'

    def add_arguments(self, parser):
        parser.add_argument('num_directors', type=int, help='Number of directors to create')

    def handle(self, *args, **options):
        num_directors = options['num_directors']
        for _ in range(num_directors):
            first_name = fake.first_name()
            last_name = fake.last_name()
            Director.objects.create(first_name=first_name, last_name=last_name)
        self.stdout.write(self.style.SUCCESS(f'Successfully created {num_directors} directors.'))
