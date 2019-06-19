from django.shortcuts import render, redirect, reverse
from django import forms
from ..models import Course, Description

class CourseForm(forms.Form):
    name = forms.CharField(max_length=255)
    desc = forms.CharField(widget=forms.Textarea)

def page(request):
    if request.method == "GET":
        form = CourseForm()

        all_courses = Course.objects.all()

        return render(request, 'course_app/main_page.html', {'form': form, 'all_courses': all_courses})

    if request.method == "POST":
        form = CourseForm(request.POST)
        errors = {}
        if form.is_valid():
            input_data = {'name': form.cleaned_data['name'],
                          'desc': form.cleaned_data['desc']}
            errors = Course.objects.validator(input_data)

            if len(errors) == 0:
                desc = Description.objects.create(content=input_data['desc'])
                Course.objects.create(name=input_data['name'], desc=desc)

                return redirect(reverse('main_page'))

        all_courses = Course.objects.all()

        return render(request, 'course_app/main_page.html', {'form': form, 'all_courses': all_courses, 'errors': errors})



