from datetime import timedelta

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from books.models import Book


def test_book_created_properly(sample_book):
    assert sample_book.title == "Sample Title"
    assert str(sample_book) == sample_book.title
    assert sample_book.category == Book.TYPE_REGULAR


def test_books_times_rented(sample_book):
    assert sample_book.times_rented == 0


def test_book_rent_created_properly(book_rent_fixture):
    assert str(book_rent_fixture) == f"Book Rent {book_rent_fixture.pk}"
    assert book_rent_fixture.books.count() == 1


def test_book_rent_charge(book_rent_fixture, book_fixture):
    assert book_rent_fixture.rent_charge == 1.5

    new_book = book_fixture(title="Fictional Book", category=Book.TYPE_FICTION)
    book_rent_fixture.days_rented = 5
    book_rent_fixture.books.add(new_book)
    book_rent_fixture.save()

    assert book_rent_fixture.rent_charge == 22.5


def test_book_in_rent_book_list(sample_book, book_rent_fixture):
    assert sample_book in book_rent_fixture.book_list


def test_book_rent_return_date(book_rent_fixture):
    ret_date = book_rent_fixture.created + timedelta(
        days=book_rent_fixture.days_rented
    )
    assert book_rent_fixture.return_date == ret_date


# ******************************************************************************************


def test_index_view(client):
    url = reverse("books:index")
    response = client.get(url)

    assert response.status_code == 200
    assertTemplateUsed == "app/app.html"
