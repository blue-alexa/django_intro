from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^books$', views.books_main_page, name='books_main_page'),
    url(r'^books/(?P<book_id>\d+)$', views.book_detail, name='book_detail'),
    url(r'books/(?P<book_id>\d+)/favorite$', views.add_to_favorite, name='add_to_favorite'),
    url(r'books/(?P<book_id>\d+)/unfavorite$', views.remove_favorite, name='remove_favorite'),
    url(r'books/(?P<book_id>\d+)/edit$', views.edit_book, name='edit_book'),
]