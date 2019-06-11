from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.book_view),
    url(r'^authors$', views.author_view),
    url(r'^books/(?P<book_id>\d+)$', views.book_detail, name="book-detail"),
    url(r'^authors/(?P<author_id>\d+)$', views.author_detail, name="author-detail"),
]