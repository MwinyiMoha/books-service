from rest_framework import serializers

from .models import Book, BookRent


class BookSerializer(serializers.ModelSerializer):
    times_rented = serializers.IntegerField(read_only=True)

    class Meta:
        model = Book
        fields = "__all__"


class BookRentSerializer(serializers.ModelSerializer):
    rent_charge = serializers.DecimalField(
        read_only=True, max_digits=10, decimal_places=2
    )
    return_date = serializers.DateTimeField(read_only=True)
    book_list = BookSerializer(many=True, read_only=True)

    class Meta:
        model = BookRent
        fields = "__all__"
