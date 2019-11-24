from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

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
                'success': 'Book \'{book}\' added successfully'.format(
                    book=book_saved.__str__()
                )
            },
            status=201,
        )

    def put(self, request, id):
        book = get_object_or_404(Book.objects.filter(id=id))
        book_upd = request.data.get('book')
        serializer = BookSerializer(instance=book, data=book_upd)
        if serializer.is_valid(raise_exception=True):
            book_saved = serializer.save()
        return Response(
            {
                'success': 'Book \'{book}\' updated successfully'.format(
                    book=book_saved.__str__()
                )
            },
            status=204,
        )

    def delete(self, request, id):
        book = get_object_or_404(Book.objects.filter(id=id))
        title = book.title
        author = book.author
        book.delete()
        return Response(
            {
                'success': 'Book \'\'{title}\' - {author}\' was deleted.'.format(  # NOQA
                    title=title, author=author
                )
            },
            status=204,
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
                'success': 'Reader {reader} added successfully'.format(
                    reader=reader_saved.__str__()
                )
            },
            status=201,
        )

    def put(self, request, id):
        reader = get_object_or_404(Reader.objects.filter(id=id))
        reader_upd = request.data.get('reader')
        serializer = BookSerializer(
            instance=reader, data=reader_upd, partial=True,
        )
        if serializer.is_valid(raise_exception=True):
            reader_saved = serializer.save()
        return Response(
            {
                'success': 'Reader {reader} updated successfully'.format(
                    reader=reader_saved.__str__()
                )
            },
        )

    def delete(self, request, id):
        reader = get_object_or_404(Reader.objects.filter(id=id))
        first_name = reader.first_name
        last_name = reader.last_name
        reader.delete()
        return Response(
            {
                'success': 'Reader {first_name} - {last_name} was deleted.'.format(  # NOQA
                    first_name=first_name, last_name=last_name
                )
            },
            status=204,
        )
