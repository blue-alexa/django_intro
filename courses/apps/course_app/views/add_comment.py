from django.shortcuts import render, redirect, reverse
from django import forms
from ..models import Course, Comment

class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)

def page(request, id):
    if request.method == "GET":
        form = CommentForm()
        course = Course.objects.get(id=id)

        return render(request, 'course_app/add_comment.html', {'form': form, 'course': course})

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            course = Course.objects.get(id=id)
            Comment.objects.create(text=text, course=course)

            return redirect(reverse('main_page'))
        else:
            course = Course.objects.get(id=id)
            return render(request, 'course_app/add_comment.html', {'form': form, 'course': course})


