from django.shortcuts import render, redirect, reverse
from ..models import Course, Description

def page(request, id):
    if request.method == "GET":
        course = Course.objects.get(id=id)

        return render(request, 'course_app/remove_course.html', {'course': course, 'id': id})

    if request.method == "POST":
        if 'yes' in request.POST:
            course = Course.objects.get(id=id)
            course.objects.delete()

        return redirect(reverse('main_page'))


