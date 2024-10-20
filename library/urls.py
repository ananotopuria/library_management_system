from django.urls import path
from .views import (
    BookListCreate,
    BookDetail,
    AuthorListCreate,
    AuthorDetail,
    GenreListCreate,
    GenreDetail
)

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('authors/', AuthorListCreate.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('genres/', GenreListCreate.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreDetail.as_view(), name='genre-detail'),
]
