from django.contrib.auth import get_user_model
import pytest

from books.models import Book, BookRent

User = get_user_model()


@pytest.fixture
def book_fixture(db):
    return Book.objects.create(
        title="Sample Title",
        author="John Doe",
        description="Short book description",
    )


@pytest.fixture
def book_rent_fixture(db, book_fixture):
    book_rent = BookRent()
    book_rent.save()

    book_rent.books.add(book_fixture)
    return book_rent


@pytest.fixture
def user_fixture(db):
    return User.objects.create_user(
        "admin", "dummy.user@dummy.com", "t0p_s3cr3t"
    )
