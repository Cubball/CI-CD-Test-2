from django.shortcuts import render

from books.models import Author, Book

def main(request):
    books = Book.objects.order_by('-publication_date').filter()[:5]
    return render(request, "book_list.html", {
        'books': books
    });

def book_detail(request, pk):
    book = Book.objects.filter(pk=pk)
    return render(request, "book_detail.html", {
        'author': book,
    })

def authors(request):
    authors = Author.objects.filter()
    return render(request, "author_list.html", {
        'authors': authors,
    })

def author_detail(request, pk):
    author = Author.objects.filter(pk=pk)
    return render(request, "author_detail.html", {
        'author': author,
    })
