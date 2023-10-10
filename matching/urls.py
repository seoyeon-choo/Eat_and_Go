from django.urls import path
from . import views

app_name = 'matching'

urlpatterns = [
    path('create_matching_room/', views.create_matching_room, name='create_matching_room'),
    path('list_matching_rooms/', views.list_matching_rooms, name='list_matching_rooms'),
    path('participate/<int:matching_room_id>/', views.participate, name='participate'),
    path('map/<int:matching_room_id>/', views.show_map, name='show_map'),

]
