from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Book, Reader
from .serializers import BookSerializer, ReaderSerializer


class BookAPIView(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({'books': serializer.data})

    def post(self, request):
        book = request.data.get('book')
        serializer = BookSerializer(data=book)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {
                'success': 'Book \'{}\' added successfully'.format(
                    book_saved.__str__()
                )
            }
        )


class ReaderAPIView(APIView):

    def get(self, request):
        readers = Reader.objects.all()
        serializer = ReaderSerializer(readers, many=True)
        return Response({'readers': serializer.data})

    def post(self, request):
        reader = request.data.get('reader')
        serializer = ReaderSerializer(data=reader)
        if serializer.is_valid(raise_exception=True):
            reader_saved = serializer.save()
        return Response(
            {
                'success': 'Reader {} added successfully'.format(
                    reader_saved.__str__()
                )
            }
        )
