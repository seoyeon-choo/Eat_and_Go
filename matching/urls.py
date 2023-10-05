from django.urls import path
from . import views

from .views import HomePageView

urlpatterns = [
    #path("", HomePageView.as_view(), name="home"),
    path('create_matching_room/', views.create_matching_room, name='create_matching_room'),
    path('', views.list_matching_rooms, name='list_matching_rooms'),
    path('participate/<int:matching_room_id>/', views.participate, name='participate'),
    path('map/<int:matching_room_id>/', views.show_map, name='show_map'),

]
