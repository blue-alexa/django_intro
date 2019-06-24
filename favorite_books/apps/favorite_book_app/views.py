from functools import wraps

from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, reverse

from .forms import BookForm
from .models import User, Book

def login(func):
    @wraps(func)
    def wrapper(request, *args, **kwds):
        if 'login' in request.session and request.session['login']:
            return func(request, *args, **kwds)
        else:
            raise PermissionDenied
    return wrapper

# Create your views here.
@login
def books_main_page(request):
    if request.method == "GET":
        form = BookForm()

        books = Book.objects.all()

        return render(request, 'favorite_book_app/main_book_page.html', {"form": form, "books": books})

    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.session['userId'])
            book = Book.objects.create(title=form.cleaned_data['title'],
                                       desc=form.cleaned_data['desc'],
                                       uploaded_by=user)
            book.users_who_like.add(user)
            return redirect(reverse('books_main_page'))
        else:
            books = Book.objects.all()
            return render(request, 'favorite_book_app/main_book_page.html', {"form": form, "books": books})


@login
def add_to_favorite(request, book_id):
    user = User.objects.get(id=request.session['userId'])
    book = Book.objects.get(id=book_id)
    book.users_who_like.add(user)
    book.save()
    return redirect(reverse('books_main_page'))

@login
def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['userId'])
    if user in book.users_who_like.all():
        unfavorite = True
    else:
        unfavorite = False
    if book.uploaded_by.id == request.session['userId']:
        form = BookForm({'title':book.title, 'desc':book.desc})
        return render(request, 'favorite_book_app/edit_book.html', {'form': form, 'book': book, 'unfavorite': unfavorite})
    else:
        return render(request, 'favorite_book_app/view_book.html', {'book': book, 'unfavorite': unfavorite})

@login
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)

    if "delete" in request.POST:
        book.delete()

    elif "update" in request.POST:
        form = BookForm({'title': request.POST['title'], 'desc': request.POST['desc']})

        user = User.objects.get(id=request.session['userId'])
        if user in book.users_who_like.all():
            unfavorite = True
        else:
            unfavorite = False

        if form.is_valid():
            book.title=form.cleaned_data['title']
            book.desc=form.cleaned_data['desc']
            book.save()

        return render(request, 'favorite_book_app/edit_book.html', {'form': form, 'book': book, 'unfavorite': unfavorite})

    return redirect(reverse('books_main_page'))

@login
def remove_favorite(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['userId'])
    book.users_who_like.remove(user)
    return redirect(reverse('book_detail', kwargs={'book_id': book_id}))