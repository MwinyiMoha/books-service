from django.contrib import admin

from .models import Book, BookRent


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "times_rented"]
    list_display_links = ["title"]


class BookRentAdmin(admin.ModelAdmin):
    list_display = ["user", "days_rented", "rent_charge", "return_date"]
    list_display_links = ["user"]


admin.site.register(Book, BookAdmin)
admin.site.register(BookRent, BookRentAdmin)
