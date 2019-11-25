from django.urls import path
from library.books.apiviews import BookAPIView, ReaderAPIView


urlpatterns = (
    path('api/books/<int:id>', BookAPIView.as_view()),
    path('api/readers/<int:id>', ReaderAPIView.as_view()),
    path('api/books/', BookAPIView.as_view()),
    path('api/readers/', ReaderAPIView.as_view()),
)
