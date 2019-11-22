from django.urls import path
from .apiviews import BookAPIView, ReaderAPIView


urlpatterns = (
    path('api/books/', BookAPIView.as_view()),
    path('api/readers/', ReaderAPIView.as_view()),
)
