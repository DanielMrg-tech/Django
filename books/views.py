import json

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from datetime import datetime
from books.models import Book
from books.serializers import BookSerializer
from books.forms import BookForm
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.


fruits = ['Apple', 'Pineapple', 'Durian', 'Passion fruit', 'Banana', 'Pear']

def hello(request):
    return HttpResponse("Hello from our Books app!")

def home(request):
    # Django -> Jinja(Template Engine)
    books = list(Book.objects.all())
    books.sort(key=(lambda x: x.date_created))

    context = {
        'username': 'Alice',
        'logged_in': True,
        'current_time': datetime.now(),
        'books': Book.objects.all()
    }

    return render(request, 'home.html', context)

def create_book(request):
    book1 = Book()
    book1.title = "Hello"
    book1.author = "Jack"
    book1.page_count = 30
    book1.save()
    return HttpResponse("DONE")

def about(request):
    return render(request, 'about.html')


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


books_list = ["X Mockingbird", "C Eminem: Greatest Hits", "D Fahrenheit 471", "A Book 1"]


def books_by_user(request: HttpRequest, user_id: int):
    books = list(Book.objects.filter(created_by = user_id))
    books.sort(key = (lambda x: x.date_created))
    context = {
        'books': books
    }
    return render(request, 'books.html', context)



@csrf_exempt
def books_view_simple(request: HttpRequest):
    if request.method == "GET":
        # Here we sort our books list:
        books_list.sort(reverse=True)
        # here we load our books in the template data context
        context = {
            "books": books_list
        }
        # here we send our template together with the context, to the jinja interpreter to be sent to our browser.
        return render(request, 'books.html', context)
    elif request.method == "POST":
        # request.body -> JSON -> dict python
        data = json.loads(request.body)
        book_title = data["title"]
        books_list.append(book_title)
        return HttpResponse("")

@csrf_exempt
@login_required
def books_view(request: HttpRequest):
    if request.method == "GET":
        context = {
            'form': BookForm()
        }
        return render(request, 'create_book.html', context)
    elif request.method == "POST":
        # request.POST -> BookForm() -> Book() -> book.save()
        form_with_data = BookForm(request.POST)
        if form_with_data.is_valid():
            # here we save our data in DB
            # BookForm() -> Book() -> book.created_by = user
            book_instance = form_with_data.save(commit=False)
            book_instance.created_by = request.user
            book_instance.save()
            return redirect('books')
        else:
            return HttpResponse(form_with_data.errors)