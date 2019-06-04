from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def generate_random_word(request):
    if request.method == "POST":
        request.session['session_sequence'] += 1
        word = get_random_string(length=14)
        request.session['last_word'] = word
        return redirect("/random_word")

    if request.method == "GET":
        if 'session_sequence' not in request.session:
            request.session['session_sequence'] = 1
        # request.session['session_sequence'] = 0
        if 'last_word' not in request.session:
            request.session['last_word'] = ""
        return render(request, "random_word/random_word.html")

def reset(request):
    try:
        del request.session['session_sequence']
        del request.session['last_word']
    except KeyError:
        pass
    return redirect("/random_word")
