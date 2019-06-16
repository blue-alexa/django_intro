from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.root),
    url(r'^shows/$', views.index, name='show_index'),
    url(r'^shows/new$', views.add_show, name='add_show'),
    url(r'^shows/create$', views.save_show, name='create_show'),
    url(r'shows/(?P<id>\d+)$', views.display_show, name='display_show'),
    url(r'shows/(?P<id>\d+)/edit$', views.edit_show, name='edit_show'),
    url(r'shows/(?P<id>\d+)/update$', views.update_show, name='update_show'),
    url(r'shows/(?P<id>\d+)/destroy$', views.delete_show, name='delete_show'),
]
