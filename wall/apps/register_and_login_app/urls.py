from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.register_or_login, name='main_page'),
    url(r'^logout$', views.logout, name='log_out')
]