from django.shortcuts import render, redirect, reverse
from django import forms
from ..models import Course, Comment

def page(request, CourseId, CommentId):
    comment = Comment.objects.get(id=CommentId)
    comment.delete()

    return redirect(reverse('display_comments', kwargs={'id': CourseId}))