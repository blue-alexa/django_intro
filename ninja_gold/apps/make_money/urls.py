from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.earn),
    url(r'^process_money$', views.process),
    url(r'^farm$', views.collect_farm),
    url(r'^cave$', views.collect_cave),
    url(r'^house$', views.collect_house),
    url(r'^casino$', views.collect_casino),
    url(r'^reset$', views.reset),
]