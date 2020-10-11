import random

from django.shortcuts import render

from .models import Items, Users,Ordered_item


def option(request):
    return render(request, "option.html")


def orderhistory(request,):
    order = Ordered_item.objects.all()
    myorders = set()
    contactno = request.session.get('contact_no')
    for i in order:
        # print(i)
        if i.contact_no == contactno:
            myorders.add(i)


    params = {"myorders": myorders}
    return render(request, "orderhistory.html", params)

def cancleorder(request,identity):
    myorders=Ordered_item.objects.get(identity=identity)
    myorders.delete()
    return render(request, "orderhistory.html")


def index(request):
    # for key in request.session.keys():
    #     del request.session[key]
    return render(request, "index.html")


def login(request):
    if request.method == "GET":
        fullname = request.GET.get('fullname', 'default')
        enrollmentno = request.GET.get("enrollmentno", 'default')
        contactno = request.GET.get("contactno", 'default')
        user_instance = Users.objects.create(enrollment_no=str(enrollmentno), user_name=str(fullname),
                                             contact_no=str(contactno))
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def home(request):
    if request.method == "GET":
        contact_no = request.GET.get("contact_no", 'default')
        users = Users.objects.all()
        for i in users:
            if i.contact_no == contact_no:
                request.session['contact_no'] = str(contact_no)
                print("51"+request.session.get('contact_no'))
                # add_order=Orders.objects.create(users=i)
                times = set()
                items = Items.objects.all()
                for i in items:
                    times.add(i.category)
                params = {"times": times}
                return render(request, "home.html", params)
    return render(request, "login.html")


def showitems(request):
    if request.method == "GET":
        context = {}
        food = set()
        ordered_food = ""
        opt = request.GET.get('timing', False)
        request.session['timing'] = str(opt)
        items = Items.objects.all()
        for i in items:
            if i.category == opt:
                food.add(i)
        # for i in food:
        #     ordered_food=","+i.name
        print(request.session.get('contact_no'))
        print(request.session.get('timing'))
        context = {"time": opt, "food": food}
    return render(request, "showitems.html", context)


def payment(request):
    total_item = 0
    total_price = 0
    food_items = []
    ordered_food = ""
    if request.method == "GET":
        items = Items.objects.all()
        for i in items:
            i.value = request.GET.get("option_" + i.name, 0)
            total_item += int(i.value)
            if int(i.value) > 0:
                total_price += int(i.price) * int(i.value)
                food_items.append(str(i.name))

        for i in food_items:
            ordered_food += "," + i
        request.session['orderd_item'] = str(ordered_food)
        request.session['total_amount'] = str(total_price)
        param = {"total_price": total_price, "total_item": total_item, "food_items": food_items}
    return render(request, "payment.html", param)


def verifyorder(request):
    return render(request, "verifyorder.html")


def successful(request):
    orderid = "order_" + str(random.randint(0, 1000))
    contactno = request.session.get('contact_no')
    preferedmenu = request.session.get('timing')
    ordereditems = request.session.get('orderd_item')
    totalamount = request.session.get('total_amount')
    add_order = Ordered_item.objects.create(identity=str(orderid), prefered_menu=preferedmenu, ordered_items=ordereditems,
                                      total_amount=totalamount, contact_no=contactno, payment_status="paid")
    return render(request, "successful.html")
