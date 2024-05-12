from ..models import Book
from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import exceptions, status
from ..serializers.bookserializer import BookSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter
import uuid
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache


class BookViewSet(ViewSet):
    """
    A ViewSet for handling book-related operations.

    Provides CRUD (Create, Retrieve, Update, Delete) operations for books.
    """

    @extend_schema(
        responses=BookSerializer(many=True), description="Retrieve all books."
    )
    @method_decorator(cache_page(60*15))
    def list(self, request: Request):
        if cache.get("book"):
            print("From cache")
        else:
            try:
                books = Book.objects.all()
            except ObjectDoesNotExist:
                raise exceptions.NotFound(
                    "Author not found", status=status.HTTP_404_NOT_FOUND
                )
            serialized_books = BookSerializer(books, many=True)
            return Response(serialized_books.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=BookSerializer,
        responses=BookSerializer(),
        description="Create a new book.",
    )
    def create(self, request: Request):
        serialized_data = BookSerializer(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id", type=str, description="UUID of the book", location="path"
            ),
        ],
        responses=BookSerializer(),
        description="Retrieve a single book by its ID.",
    )
    def retrive(self, request: Response, pk: uuid.uuid4):
        try:
            book = Book.objects.get(book_id=pk)
        except Book.DoesNotExist:
            raise exceptions.NotFound(
                f"Book with id {id} not found.", status=status.HTTP_404_NOT_FOUND
            )
        serialized_data = BookSerializer(data=book)
        return Response(serialized_data.data)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id", type=str, description="UUID of the book", location="path"
            )
        ],
        request=BookSerializer,
        responses=BookSerializer(),
        description="Update a Book.",
    )
    def update(self, request: Request, id: uuid.uuid4):
        try:
            book_instance = Book.objects.get(book_id=id)
        except Book.DoesNotExist:
            raise exceptions.NotFound(f"Book with id {id} not found.")
        serialized_data = BookSerializer(instance=book_instance, data=request.data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)

        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id", type=str, description="UUID of the book", location="path"
            )
        ],
        request=BookSerializer,
        responses=BookSerializer(),
        description="Update a Book.",
    )
    def partial_update(self, request: Request, id: uuid.uuid4):
        try:
            book_instance = Book.objects.get(book_id=id)
        except Book.DoesNotExist:
            raise exceptions.NotFound(f"Book with id {id} not found.")
        serialized_data = BookSerializer(
            instance=book_instance, data=request.data, partial=True
        )
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)

        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="id", type=str, description="UUID of the book", location="path"
            ),
        ],
        description="Delete a book by its ID.",
    )
    def destroy(self, request: Request, pk: uuid.uuid4):
        try:
            book_instance = Book.objects.get(book_id=pk)
        except Book.DoesNotExist:
            raise exceptions.NotFound(f"Book with id {pk} not found.")
        book_instance.delete()
        return Response(
            f"Book with id {id} deleted successfully", status=status.HTTP_204_NO_CONTENT
        )
