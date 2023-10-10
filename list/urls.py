from django.urls import path
from . import views

app_name = 'list'

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('<int:id>/<slug:slug>/', views.menu_detail, name='menu_detail'),
]
