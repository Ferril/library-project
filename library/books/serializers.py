from rest_framework import serializers
from .models import Book, Reader


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, required=True)
    author = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(required=False)
    reader = serializers.CharField(required=False)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)


class ReaderSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    list_of_books = serializers.ListField()

    def create(self, validated_data):
        return Reader.objects.create(**validated_data)
