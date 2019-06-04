from django.shortcuts import render, redirect

def index(request):
    context = {
        "place_holder": "placeholder to later display a list of all blogs."
    }
    return render(request, "blogs_app/index.html", context)

def new(request):
    context = {
        "place_holder": "placeholder to display a new form to create a new blog."
    }
    return render(request, "blogs_app/new_blog.html", context)

def create(request):
    return redirect("/blogs/new")

def show(request, number):
    context = {
        "number": number
    }
    return render(request, "blogs_app/single_blog.html", context)

def edit(request, number):
    context = {
        "number": number
    }
    return render(request, "blogs_app/edit_blog.html", context)

def destroy(request, number):
    pass
    return redirect("/blogs")

# Create your views here.
