from django.urls import path
from .views import *

urlpatterns = [
    path('', StartPage.as_view(), name='start_page'),
    path('books/', BookList.as_view(), name='book_list'),
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('book/detail/<slug:book_slug>/', BookDetail.as_view(), name='book_detail'),
    path('author/detail/<slug:slug>/', AuthorDetail.as_view(), name='author_detail'),
    path('create/book/', BookCreate.as_view(), name='create_book'),
    path('create/author/', AuthorCreate.as_view(), name='create_author'),
    path('update/book/<slug:slug>/', BookUpdate.as_view(), name='update_book'),
    path('update/author/<slug:slug>/', AuthorUpdate.as_view(), name='update_author'),
    path('delete/book/<slug:slug>/', BookDelete.as_view(), name='delete_book'),
    path('delete/author/<slug:slug>/', AuthorDelete.as_view(), name='delete_author'),
]