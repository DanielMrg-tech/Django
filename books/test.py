import pytest
from books.models import Book
from django.contrib.auth import get_user_model


@pytest.fixture
def user(db):
    return get_user_model().objects.create_user(username = 'daniel', password='daniel12345')

@pytest.fixture
def logged_in_client(client, user):
    return client.login(username=user.name, password=user.password)


def test_book_creation(db, user):
   saved_book = Book.objects.create(title='Book hello', author="Test", page_count=300, created_by= user)

   db_book = Book.objects.first()
   assert saved_book.title == db_book.title

def test_user_login(user):
    pass


@pytest.fixture
def book_obj():
    book1 = Book(title="Book 1", author='Jamal', page_count=300)
    return book1

def test_check_thing1(book_obj):
    assert book_obj.book1.title == 'Book 1'
    assert True


def test_check_book(book_obj):
    assert book_obj.author == 'Jamal'