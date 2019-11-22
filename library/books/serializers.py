from rest_framework import serializers


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    description = serializers.CharField()
    reader = serializers.CharField()


class ReaderSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    list_of_books = serializers.ListField()
