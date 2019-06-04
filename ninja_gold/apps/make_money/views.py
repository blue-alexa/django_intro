from django.shortcuts import render, redirect
import random
import datetime

def earn(request):
    if request.method == "POST":
        print(request.POST)
        if 'goal' in request.POST:
            # reset history when goal is set.
            request.session['history'] = []
            request.session['total'] = 0
            request.session['goal'] = request.POST['goal']
            request.session['result'] = ""

        return render(request, "make_money/index.html")

    if request.method == "GET":
        if 'history' not in request.session:
            request.session['history'] = []

        if 'total' not in request.session:
            request.session['total'] = 0

        print(request.GET)

        return render(request, "make_money/index.html")

amount_dict = {
    'farm': (10, 20),
    'cave': (5, 10),
    'house': (2, 5),
    'casino': (-50, 50),
}
def calculate(location, request):
    lo, hi = amount_dict[location]
    amount = random.randint(lo, hi)
    current_time = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
    request.session['history'].append((location, amount, current_time))
    request.session['total'] += amount
    return request

def collect_farm(request):
    calculate('farm', request)
    return redirect("/process_money")

def collect_cave(request):
    calculate('cave', request)
    return redirect("/process_money")

def collect_house(request):
    calculate('house', request)
    return redirect("/process_money")

def collect_casino(request):
    calculate('casino', request)
    return redirect("/process_money")

def process(request):
    if 'goal' in request.session and 'total' in request.session:
        if int(request.session['goal']) <= request.session['total']:
            request.session['result'] = 'You win!'

    if 'total' in request.session and request.session['total'] < 0:
        request.session['result'] = 'You lost!'

    return redirect("/")

def reset(request):
    request.session['history'] = []
    request.session['total'] = 0
    request.session['result'] = ""
    try:
        del request.session['goal']
    except KeyError:
        pass
    return redirect("/")