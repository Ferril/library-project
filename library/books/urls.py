from django.urls import path
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view
from books.apiviews import BookAPIView, ReaderAPIView

schema_view = get_swagger_view(title='Books API')


urlpatterns = (
    path('api/books/<int:book_id>', BookAPIView.as_view()),
    path('api/readers/<int:reader_id>', ReaderAPIView.as_view()),
    path('api/books/', BookAPIView.as_view()),
    path('api/readers/', ReaderAPIView.as_view()),
    url(r'^$', schema_view),
)
