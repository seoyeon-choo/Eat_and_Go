from django.shortcuts import render, get_object_or_404
from .models import Menu
from cart.forms import AddProductForm

def menu_list(request):
    menus = Menu.objects.filter(available_display=True)
    return render(request, 'list/buy_list.html', {'menus': menus})

def menu_detail(request, id, slug):
    menu = get_object_or_404(Menu, id=id, slug=slug, available_display=True)
    add_to_cart = AddProductForm(initial={'quantity': 1})
    return render(request, 'list/buy_detail.html', {'menu': menu, 'add_to_cart': add_to_cart})

def menu_list(request):
    return render(request, 'list/buy_list.html')


# def success_view(request): #html을 보여주는 함수(여기다가 html 걸면 될듯~~)
#     return render(request, 'gift/success.html')