from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.root.page, name='main_page'),
    url(r'^courses/destroy/(?P<id>\d+)$', views.remove_course.page, name='remove_course'),
    url(r'^courses/(?P<id>\d+)/comment$', views.add_comment.page, name='add_comment'),
    url(r'^courses/(?P<id>\d+)/comments/$', views.display_comments.page, name='display_comments'),
    url(r'^courses/(?P<CourseId>\d+)/comment/(?P<CommentId>\d+)/destroy$', views.delete_comment.page, name='delete_comment'),
]