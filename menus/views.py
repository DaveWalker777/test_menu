from django.shortcuts import render


def index(request):
    return render(request, 'menus/index.html')


def page_one(request):
    return render(request, 'menus/page_one.html')


def page_two(request):
    return render(request, 'menus/page_two.html')


def page_three(request):
    return render(request, 'menus/page_three.html')


def sub_1(request):
    return render(request, 'menus/sub_1.html')

