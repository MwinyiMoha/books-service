from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from core.models import BaseModel

User = get_user_model()


class Book(BaseModel):
    title = models.CharField(max_length=99)
    author = models.CharField(max_length=99)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def times_rented(self):
        return self.bookrent_set.count()


class BookRent(BaseModel):
    # user = models.ForeignKey(User, on_delete=models.PROTECT)

    books = models.ManyToManyField(Book)
    days_rented = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return f"Book Rent By {self.user.username}"

    @property
    def rent_charge(self):
        return self.days_rented * self.books.count() * 1

    @property
    def book_list(self):
        return self.books.all()

    @property
    def return_date(self):
        return self.created + timedelta(days=self.days_rented)
