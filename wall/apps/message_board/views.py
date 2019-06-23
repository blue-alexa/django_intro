from functools import wraps

from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, reverse
from django import forms

from .models import Message, Comment
from ..register_and_login_app.models import User

def login(func):
    @wraps(func)
    def wrapper(request, *args, **kwds):
        if 'login' in request.session and request.session['login']:
            return func(request, *args, **kwds)
        else:
            raise PermissionDenied
    return wrapper

class MessgaeForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea())

class CommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea())

@login
def main_page(request):
    if request.method == "GET":
        mform = MessgaeForm()
        cform = CommentForm()
        messages = Message.objects.all().order_by('-created_at')
        return render(request, 'message_board/main_page.html', {'messages': messages, 'mform': mform, 'cform': cform})

@login
def add_message(request):
    if request.method == "POST":
        print(request.POST)
        mform = MessgaeForm(request.POST)
        if mform.is_valid():
            message = mform.cleaned_data['message']
            user_id = request.session['userId']
            user = User.objects.get(id=user_id)

            Message.objects.create(user_id=user, message=message)

            return redirect(reverse('main_message_page'))

        else:
            cform = CommentForm()
            messages = Message.objects.all().order_by('-created_at')
            return render(request, 'message_board/main_page.html', {'messages': messages, 'mform': mform, 'cform': cform})

@login
def add_comment(request):
    if request.method == "POST":
        message_id = request.POST['submit']
        print(request.POST)
        cform = CommentForm({'comment':request.POST['comment']})
        if cform.is_valid():
            comment = cform.cleaned_data['comment']
            message = Message.objects.get(id=message_id)
            user = User.objects.get(id=request.session['userId'])
            if message:
                Comment.objects.create(message_id=message, user_id = user, comment=comment)

            return redirect(reverse('main_message_page'))
        else:
            mform = MessgaeForm()
            messages = Message.objects.all().order_by('-created_at')
            return render(request, 'message_board/main_page.html', {'messages': messages, 'mform': mform, 'cform': cform})

@login
def delete_message(request, message_id):
    message = Message.objects.get(id=message_id)
    message.delete()
    return redirect(reverse('main_message_page'))




@login
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect(reverse('main_message_page'))





