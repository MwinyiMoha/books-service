from datetime import timedelta
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from core.models import BaseModel

User = get_user_model()


class Book(BaseModel):

    TYPE_FICTION = "fiction"
    TYPE_REGULAR = "regular"
    TYPE_NOVEL = "novel"

    TYPE_CHOICES = (
        (TYPE_FICTION, "Fiction"),
        (TYPE_REGULAR, "Regular"),
        (TYPE_NOVEL, "Novel"),
    )

    title = models.CharField(max_length=99)
    author = models.CharField(max_length=99)
    description = models.TextField(null=True, blank=True)
    category = models.CharField(
        max_length=7, choices=TYPE_CHOICES, default=TYPE_REGULAR
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, default=Decimal("1.5")
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if (
            self.category == self.TYPE_NOVEL
            or self.category == self.TYPE_REGULAR
        ):
            self.price = 1.5
        else:
            self.price = 3.0

        super(Book, self).save(*args, **kwargs)

    def calculate_charge(self, no_of_days):
        charge = None

        if self.category == self.TYPE_FICTION:
            charge = self.price * no_of_days
        elif self.category == self.TYPE_REGULAR:
            min_charge = 2.0
            if no_of_days <= 2:
                charge = min_charge
            else:
                extra = (no_of_days - 2) * 1.5
                charge = Decimal((min_charge + extra))
        else:
            min_charge = 4.5
            if no_of_days <= 3:
                charge = min_charge
            else:
                extra = (no_of_days - 3) * 1.5
                charge = Decimal((min_charge + extra))

        return charge

    @property
    def times_rented(self):
        return self.bookrent_set.count()


class BookRent(BaseModel):
    books = models.ManyToManyField(Book)
    days_rented = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return f"Book Rent {self.pk}"

    @property
    def rent_charge(self):
        return sum(
            [i.calculate_charge(self.days_rented) for i in self.books.all()]
        )

    @property
    def book_list(self):
        return self.books.all()

    @property
    def return_date(self):
        return self.created + timedelta(days=self.days_rented)
