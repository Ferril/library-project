from django.contrib import admin

from library.books.models import Book, Reader

admin.site.register(Book)
admin.site.register(Reader)
