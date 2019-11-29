from django.urls import path
from books.apiviews import BookAPIView, ReaderAPIView


urlpatterns = (
    path('api/books/<int:book_id>', BookAPIView.as_view()),
    path('api/readers/<int:reader_id>', ReaderAPIView.as_view()),
    path('api/books/', BookAPIView.as_view()),
    path('api/readers/', ReaderAPIView.as_view()),
)
