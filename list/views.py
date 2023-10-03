from django.shortcuts import render, get_object_or_404
from .models import *
from cart.forms import AddProductForm

# Create your views here.

def menu_in_category(request, category_slug=None):
    current_category = None
    categories = Buycategory.objects.all()
    products = Menu.objects.filter(available_display=True)

    if category_slug:
        current_category = get_object_or_404(Buycategory, slug=category_slug)
        products = products.filter(category=current_category)

    return render(request, 'shop/buy_list.html', {'current_category': current_category, 'categories':categories, 'products':products})

def menu_detail(request, id, product_slug=None):
    product = get_object_or_404(Menu, id=id, slug=product_slug)
    add_to_cart = AddProductForm(initial={'quantity' : 1})
    return render(request, 'shop/buy_detail.html', {'product': product, 'add_to_cart' : add_to_cart})

