from rest_framework.viewsets import ViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from ..models import Loan
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import exceptions, status
from ..serializers.loanserializer import LoanSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter


class BookLoanViewSet(ViewSet):
    """
    A ViewSet for handling book loan related operations.

    Provides CRUD (Create, Retrieve, Update, Delete) operations for books.
    """

    @extend_schema(responses=LoanSerializer, description="Retrives all loans.")
    def list(self, request: Request):
        try:
            loans = Loan.objects.all()
        except ObjectDoesNotExist:
            raise exceptions.NotFound(
                "Loan not found", status=status.HTTP_404_NOT_FOUND
            )
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=LoanSerializer,
        responses=LoanSerializer(),
        description="Create a new loan.",
    )
    def create(self, request: Request):
        serializer = LoanSerializer(request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
