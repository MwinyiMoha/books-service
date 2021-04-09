from datetime import timedelta

from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


def test_book_created_properly(book_fixture):
    assert book_fixture.title == "Sample Title"
    assert str(book_fixture) == book_fixture.title


def test_books_times_rented(book_fixture):
    assert book_fixture.times_rented == 0


def test_book_rent_created_properly(book_rent_fixture):
    assert str(book_rent_fixture) == f"Book Rent {book_rent_fixture.pk}"
    assert book_rent_fixture.books.count() == 1


def test_book_rent_charge(book_rent_fixture):
    assert book_rent_fixture.rent_charge == 1.00

    book_rent_fixture.days_rented = 5
    book_rent_fixture.save()

    assert book_rent_fixture.rent_charge == 5.00


def test_book_in_rent_book_list(book_fixture, book_rent_fixture):
    assert book_fixture in book_rent_fixture.book_list


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
