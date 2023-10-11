from django.shortcuts import render, get_object_or_404
from .models import Menu
from cart.forms import AddProductForm
from django.shortcuts import render


def menu_list(request):
    menus = Menu.objects.filter(available_display=True)
    return render(request, 'list/buy_list.html', {'menus': menus})

def menu_detail(request, id, slug):
    add_to_cart = AddProductForm(initial={'quantity': 1})
    return render(request, 'list/buy_detail.html')

def menu_list(request):
    return render(request, 'list/buy_list.html')
def review(request):

    return render(request, 'list/review.html')


def write_review(request):
    
    return render(request, 'list/write_review.html')


# def success_view(request): #html을 보여주는 함수(여기다가 html 걸면 될듯~~)
#     return render(request, 'gift/success.html')