from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from books.models import Author, Book

class Tests(TestCase):
    def setUp(self):
        self.authors = [Author.objects.create(name="Author 1", bio=""),Author.objects.create(name="Author 2", bio="")]
        self.book = Book.objects.create(title="Book 1", description="", publication_date="2024-01-01", cover_image=SimpleUploadedFile(name='1.png', content=''), price=100)
        self.book.authors.set(self.authors)

    def test_books_list_view_returns_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'book_list.html')

    def test_books_list_view_returns_books(self):
        response = self.client.get('/')
        self.assertContains(response, self.book.title)
