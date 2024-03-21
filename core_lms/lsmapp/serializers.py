import uuid
from .models import Author, Book, Loan
from rest_framework import serializers


class AuthonSerializer(serializers.Serializer):
    author_id = serializers.UUIDField(required=False, allow_null=True)
    name = serializers.CharField(max_length=50)
    nationality = serializers.CharField(max_length=50)
    birth_year = serializers.DateField(allow_null=True, required=False)
    print("hello")

    def create(self, validated_data) -> Author:
        print("print from create")
        try:
            author = Author.objects.create(**validated_data)
        except Exception as e:
            raise e
        return author

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.nationality = validated_data.get("nationality", instance.nationality)
        instance.birth_year = validated_data.get("birth_year", instance.birth_year)
        instance.save()
        return instance
