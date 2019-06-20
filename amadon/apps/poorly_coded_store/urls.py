from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^checkout/(?P<id>\d+)$', views.checkout, name="checkout"),
]