from ..models import Book
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import exceptions, status
from ..serializers.bookserializer import BookSerializer


class BookViewSet(ViewSet):
    """
    A ViewSet for handling book-related operations.

    Provides CRUD (Create, Retrieve, Update, Delete) operations for books.
    """

    def list(self, request: Request):
        try:
            books = Book.objects.all()
        except ObjectDoesNotExist:
            raise exceptions.NotFound(
                "Author not found", status=status.HTTP_404_NOT_FOUND
            )
        serialized_books = BookSerializer(books, many=True)
        return Response(serialized_books.data, status=status.HTTP_200_OK)
