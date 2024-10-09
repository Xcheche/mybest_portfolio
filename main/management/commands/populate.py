import random
from faker import Faker
from django.core.management.base import BaseCommand
from main.models import About, Education, Experience, Service  # Import your models
from main.models import Status  # Import the Status choices if needed

# Initialize Faker
fake = Faker()

class Command(BaseCommand):
    help = "Populates the database with fake data for About, Education, Experience, and Service models"

    def handle(self, *args, **kwargs):
        # Clear existing data (optional)
        About.objects.all().delete()
        Education.objects.all().delete()
        Experience.objects.all().delete()
        Service.objects.all().delete()

        # Populate About model (single instance for portfolio)
        about = About.objects.create(
            body=fake.text(max_nb_chars=500),
            image='',  # You can leave this blank or add a default image path
            status=random.choice([Status.DRAFT, Status.PUBLISHED])
        )
        self.stdout.write(self.style.SUCCESS(f'Added About: {about.body[:30]}...'))

        # Populate Education model
        for _ in range(3):  # Add 3 fake education entries
            education = Education.objects.create(
                title=fake.job(),
                date=fake.year(),
                body=fake.text(max_nb_chars=500),
                status=random.choice([Status.DRAFT, Status.PUBLISHED])
            )
            self.stdout.write(self.style.SUCCESS(f'Added Education: {education.title}'))

        # Populate Experience model
        for _ in range(3):  # Add 3 fake experience entries
            experience = Experience.objects.create(
                title=fake.company(),
                date=fake.date_this_decade(),
                location=fake.city(),
                position=fake.job(),
                body=fake.text(max_nb_chars=500),
                status=random.choice([Status.DRAFT, Status.PUBLISHED])  # Corrected this line
            )
            self.stdout.write(self.style.SUCCESS(f'Added Experience: {experience.title}'))

        # Populate Service model
        for _ in range(3):  # Add 3 fake service entries
            service = Service.objects.create(
                title=fake.bs(),  # Use a short phrase for service title
                body=fake.text(max_nb_chars=500),
                status=random.choice([Status.DRAFT, Status.PUBLISHED])
            )
            self.stdout.write(self.style.SUCCESS(f'Added Service: {service.title}'))

        self.stdout.write(self.style.SUCCESS('Database population complete.'))
