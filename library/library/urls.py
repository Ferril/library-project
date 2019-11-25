from django.contrib import admin
from django.urls import path, include

app_name = 'books'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
]
