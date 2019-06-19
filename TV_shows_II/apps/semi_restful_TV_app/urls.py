from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^$', views.root),
    url(r'^shows/$', views.index.page, name='index'),
    url(r'^shows/new$', views.create_show.page, name='create_show'),
    url(r'^shows/create$', views.save_show.page, name='save_show'),
    url(r'shows/(?P<id>\d+)$', views.display_show.page, name='display_show'),
    url(r'shows/(?P<id>\d+)/edit$', views.edit_show.page, name='edit_show'),
    url(r'shows/(?P<id>\d+)/update$', views.update_show.page, name='update_show'),
    url(r'shows/(?P<id>\d+)/destroy$', views.delete_show.page, name='delete_show'),
]