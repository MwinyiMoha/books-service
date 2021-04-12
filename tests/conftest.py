from django.contrib.auth import get_user_model
import pytest

from books.models import Book, BookRent

User = get_user_model()


@pytest.fixture
def book_fixture(db):
    def create_book(**kwargs):
        return Book.objects.create(
            title=kwargs["title"],
            category=kwargs["category"],
            author="John Doe",
            description="Short book description",
        )

    return create_book


@pytest.fixture
def sample_book(db, book_fixture):
    book = book_fixture(title="Sample Title", category=Book.TYPE_REGULAR)

    return book


@pytest.fixture
def book_rent_fixture(db, sample_book):
    book_rent = BookRent()
    book_rent.save()

    book_rent.books.add(sample_book)
    return book_rent


@pytest.fixture
def user_fixture(db):
    return User.objects.create_user(
        "admin", "dummy.user@dummy.com", "t0p_s3cr3t"
    )
