from rest_framework import routers

from books.views import BookViewSet, BookRentViewSet

router = routers.DefaultRouter()
router.register("books", BookViewSet)
router.register("book-rents", BookRentViewSet)

urlpatterns = []

urlpatterns += router.urls
