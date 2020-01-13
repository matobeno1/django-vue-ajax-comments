from django.urls import path
from django.views.generic import RedirectView

from .views import BookListView, book_detail_view, book_detail_view_ajax

# This is a namespace for the `books` app/module.
name = "books"

urlpatterns = [
    path("", RedirectView.as_view(url="/books")),
    path("books/", BookListView.as_view(), name='booklist'),
    path("books/<int:pk>", book_detail_view, name="book_detail"),
]
