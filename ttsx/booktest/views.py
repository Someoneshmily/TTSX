from django.shortcuts import render

# Create your views here.


def cart(request):
    return render(request,'booktest/cart.html')


def detail(request):
    return render(request,'booktest/detail.html')


def index(request):
    return render(request,'booktest/index.html')


def list(request):
    return render(request,'booktest/list.html')


def login(request):
    return render(request,'booktest/login.html')


def place_order(request):
    return render(request,'booktest/place_order.html')


def register(request):
    return render(request,'booktest/register.html')


def user_center_info(request):
    return render(request,'booktest/user_center_info.html')


def user_center_order(request):
    return render(request,'booktest/user_center_order.html')


def user_center_site(request):
    return render(request,'booktest/user_center_site.html')