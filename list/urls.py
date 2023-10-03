from django.urls import path
from .views import *

app_name = 'list'

urlpatterns = [
    path('', menu_in_category, name='menu_all'),
    # path('<slug:category_slug>/', product_in_category, name='product_on_category'),
    path('<category_slug>/', menu_in_category, name='menu_in_category'),
    path('<int:id>/<product_slug>/', menu_detail, name='menu_detail'),
]