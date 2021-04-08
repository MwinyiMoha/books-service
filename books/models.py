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


class BookRent(BaseModel):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    books = models.ManyToManyField(Book)
    days_rented = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return f"Book Rent By {self.user.username}"
