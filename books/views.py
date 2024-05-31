from django.shortcuts import render

from books.models import Author, Book

def main(request):
    books = Book.objects.order_by('-publication_date').filter()[:5]
    return render(request, "book_list.html", {
        'books': books
    });

def authors(request):
    authors = Author.objects.filter()
    return render(request, "author_list.html", {
        'authors': authors,
    })
