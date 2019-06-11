from django.shortcuts import render, redirect
from .models import Books, Authors

def book_view(request):
    if request.method == "GET":
        context = {
            "all_books": Books.objects.all()
        }
        return render(request, "books_and_authors_app/book_view.html", context)

    if request.method == "POST":
        # add new book to the db
        title = request.POST['title']
        desc = request.POST['desc']
        Books.objects.create(title=title, desc=desc)
        
        context = {
            "all_books": Books.objects.all()
        }
        
        return render(request, "books_and_authors_app/book_view.html", context)

def author_view(request):
    if request.method == "GET":
        context = {
            "all_authors": Authors.objects.all()
        }
        return render(request, "books_and_authors_app/author_view.html", context)

    if request.method == "POST":
        # add new author to db
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        notes = request.POST['notes']
        Authors.objects.create(first_name=first_name, last_name=last_name, notes=notes)

        context = {
            "all_authors": Authors.objects.all()
        }
        return render(request, "books_and_authors_app/author_view.html", context)

def book_detail(request, book_id):
    if request.method == "GET":
        book = Books.objects.get(id=book_id)
        all_authors = Authors.objects.all()
        context = {
            "book": book,
            "all_authors": all_authors,
        }
        return render(request, "books_and_authors_app/book_detail.html", context)

    if request.method == "POST":
        author_id = request.POST['select_author']
        # add author to current book
        book = Books.objects.get(id=book_id)
        author = Authors.objects.get(id=author_id)
        book.authors.add(author)
        book.save()

        return redirect(request.path_info) #redirect to the same page

def author_detail(request, author_id):
    if request.method == "GET":
        author = Authors.objects.get(id=author_id)
        all_books = Books.objects.all()
        context = {
            "author": author,
            "all_books": all_books,
        }
        return render(request, "books_and_authors_app/author_detail.html", context)

    if request.method == "POST":
        book_id = request.POST['select_book']
        # add author to current book
        book = Books.objects.get(id=book_id)
        author = Authors.objects.get(id=author_id)
        book.authors.add(author)
        book.save()

        return redirect(request.path_info) #redirect to the same page
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# Create your views here.
