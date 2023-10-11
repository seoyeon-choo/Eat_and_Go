from django.urls import path
from . import views

app_name = 'list'

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
     path('review/', views.review, name='review'),
    path('<int:id>/<slug:slug>/', views.menu_detail, name='menu_detail'),
    path('write_review/', views.write_review, name='write_review')

]
