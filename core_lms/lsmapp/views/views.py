from ..models import Author
from rest_framework import exceptions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from ..serializers.serializers import AuthonSerializer
import uuid
from django.core.exceptions import ObjectDoesNotExist


class AuthorViewSet(APIView):
    def get(self, request: Request, id: uuid.uuid4 = None) -> Response:
        "Retrive all author object"
        try:
            if id is not None:
                requested_author = Author.objects.get(author_id=id)
                serialized_data = AuthonSerializer(requested_author)
                return Response(serialized_data.data, status=status.HTTP_200_OK)

            authors = Author.objects.all()
            serialized_data = AuthonSerializer(authors, many=True)
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            raise exceptions.NotFound("Author not found")

    def post(self, request: Request) -> Response:
        serialized_data = AuthonSerializer(data=request.data)

        if not serialized_data.is_valid():
            raise exceptions.ValidationError(serialized_data.errors)
        serialized_data.save()
        return Response(serialized_data.data)

    def put(self, request: Request, id: uuid.uuid4) -> Response:
        try:
            request_author = Author.objects.get(author_id=id)
        except ObjectDoesNotExist:
            raise exceptions.NotFound("Author not found")

        serialized_data = AuthonSerializer(
            instance=request_author, data=request.data, partial=True
        )

        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)

        raise exceptions.ValidationError(
            serialized_data.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        try:
            book = Author.objects.get(author_id=id)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        book.delete()
        return Response(f"Delete author with id{id}", status=status.HTTP_204_NO_CONTENT)
