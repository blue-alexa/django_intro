from django.shortcuts import render, redirect, reverse
from ..models import Course, Comment

def page(request, id):
    if request.method == "GET":
        course = Course.objects.get(id=id)

        return render(request, 'course_app/display_comments.html', {'course': course})
