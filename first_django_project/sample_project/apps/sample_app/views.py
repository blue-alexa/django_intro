from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs.")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect("/")

def show(request, number):
    return HttpResponse("placeholder to display blog number: %s"%number)

def edit(request, number):
    return HttpResponse("placeholder to edit blog %s"%number)

def destroy(request, number):
    return redirect("/")