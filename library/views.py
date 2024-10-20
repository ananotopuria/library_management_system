from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return HttpResponse("Book not found", status=404)

    return render(request, 'library/book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')

        new_book = Book(title=title, author=author)
        new_book.save()

        return HttpResponse("Book added successfully", status=201)
    else:
        return render(request, 'library/add_book.html')


