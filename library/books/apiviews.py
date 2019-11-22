from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Reader
from .serializers import BookSerializer, ReaderSerializer


class BookAPIView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"books": serializer.data})


class ReaderAPIView(APIView):

    def get(self, request):
        readers = Reader.objects.all()
        # list_of_books = [reader.list_of_books for reader in readers]
        # print(list_of_books)
        serializer = ReaderSerializer(readers, many=True)
        return Response({"readers": serializer.data})
