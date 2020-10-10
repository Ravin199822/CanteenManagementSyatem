from django.shortcuts import render

from .models import Items


def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def home(request):
    times = set()
    items = Items.objects.all()
    for i in items:
        times.add(i.category)
    params = {"times": times}
    return render(request, "home.html", params)


def showitems(request):
    if request.method == "GET":
        context = {}
        food = set()
        opt = request.GET.get('timing', False)
        items = Items.objects.all()
        for i in items:
            if i.category == opt:
                food.add(i)
        print(food)
        context = {"time": opt, "food": food}
    return render(request, "showitems.html", context)


def payment(request):
    total_item = 0
    total_price = 0
    food_items=[]
    if request.method == "GET":
        items = Items.objects.all()
        for i in items:
            i.value = request.GET.get("option_" + i.name, 0)
            total_item += int(i.value)
            if int(i.value) > 0:
                total_price += int(i.price) * int(i.value)
                food_items.append(str(i.name))
        param={"total_price":total_price,"total_item":total_item, "food_items":food_items}
    return render(request, "payment.html",param)


def successful(request):
    return render(request, "successful.html")
