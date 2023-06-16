import requests
from django.core.management.base import BaseCommand
from book_review.models import Book
from datetime import datetime

class Command(BaseCommand):
    help = "Fill in Book model with data"

    # You can perform a volumes search by sending an HTTP GET request to the following URI:
    # https://www.googleapis.com/books/v1/volumes?q=search+terms

    def handle(self, *args, **options):
        response = requests.get('https://www.googleapis.com/books/v1/volumes?q=intitle:google')
        data = response.json()

        for item in data['items']:
            volume_info = item['volumeInfo']

            book=Book()
            book.title=volume_info.get('title', '')
            book.author = ', '.join(volume_info.get('authors', []))
            # Handle date format
            published_date = volume_info.get('publishedDate', '')
            try:
                book.published_date = datetime.strptime(published_date, '%Y-%m-%d').date()
            except ValueError:
                book.published_date = None
            book.description = volume_info.get('description', '')
            book.page_count = volume_info.get('pageCount', 0)
            book.categories = ', '.join(volume_info.get('categories', []))
            # Handle missing thumbnail URL
            image_links = volume_info.get('imageLinks')
            if image_links and 'thumbnail' in image_links:
                book.thumbnail_url = image_links['thumbnail']
            else:
                book.thumbnail_url = ''
            book.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated Book model with data from Google Books API.'))