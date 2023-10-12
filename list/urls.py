from django.urls import path
from . import views

app_name = 'list'

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('review/', views.review, name='review'),
    path('menu_cart/', views.menu_cart, name='menu_cart'),
    path('ticket_using/', views.ticket_using, name='ticket_using'),
    path('order_done/', views.order_done, name='order_done'),
    path('<int:id>/<slug:slug>/', views.menu_detail, name='menu_detail'),
    path('write_review/', views.write_review, name='write_review')

]
