from django.core.management.base import BaseCommand
from faker import Faker
from datetime import timedelta, date
from rent.models import Rental, Vehicle

fake = Faker()

class Command(BaseCommand):
    help = 'Generate 100 rentals with random data'

    def handle(self, *args, **options):
        vehicles = Vehicle.objects.all()
        today = date.today()
        start_date = today - timedelta(days=365)  # 1 year ago

        for _ in range(100):
            rental_date = fake.date_between_dates(date_start=start_date, date_end=today)
            vehicle = vehicles.filter(rental__isnull=True).first()

            if vehicle:
                rental_duration = fake.random_int(min=1, max=7)  # Random rental duration in days
                return_date = rental_date + timedelta(days=rental_duration)

                if fake.boolean(chance_of_getting_true=20):
                    return_date = None

                Rental.objects.create(
                    rental_date=rental_date,
                    return_date=return_date,
                    customer_id=fake.random_int(min=1, max=100),
                    vehicle=vehicle
                )

        self.stdout.write(self.style.SUCCESS('Successfully created 100 rentals.'))
