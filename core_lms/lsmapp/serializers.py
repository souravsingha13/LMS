from .models import Author,Book,Loan
from rest_framework import serializers


class AuthonSerializer(serializers.Serializer):
    author_id = serializers.UUIDField()
    name = serializers.CharField(max_lenght = 50)
    nationality = serializers.CharField(max_length=50)
    birth_year = serializers.DateField(allow_null=True, required=False)
    
    def create(self, validated_data):
        author = Author.objects.create(**validated_data)
        return author

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    

