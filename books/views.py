from rest_framework import viewsets

from .models import Book, BookRent
from .serializers import BookSerializer, BookRentSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRentViewSet(viewsets.ModelViewSet):
    queryset = BookRent.objects.all().select_related().prefetch_related()
    serializer_class = BookRentSerializer
