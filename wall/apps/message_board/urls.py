from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^messages$', views.main_page, name='main_message_page'),
    url(r'^message/new$', views.add_message, name='add_message'),
    url(r'^comment/new$', views.add_comment, name='add_comment'),
    url(r'message/(?P<message_id>\d+)/delete$', views.delete_message, name='delete_message'),
    url(r'comment/(?P<comment_id>\d+)/delete$', views.delete_comment, name='delete_comment'),
]
