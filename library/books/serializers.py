from rest_framework import serializers
from .models import Book, Reader


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100, required=True)
    author = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(required=False)
    reader = serializers.CharField(required=False)

    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.description = validated_data.get(
            'description', instance.description,
        )
        instance.reader = validated_data.get('reader', instance.reader)
        instance.save()
        return instance


class ReaderSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    list_of_books = serializers.ListField(required=False)

    def create(self, validated_data):
        return Reader.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            'first_name', instance.first_name,
        )
        instance.last_name = validated_data.get(
            'last_name', instance.last_name,
        )
        instance.save()
        return instance
