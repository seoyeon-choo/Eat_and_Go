from django.urls import path, include
from . import views, admin
from django.contrib import admin

app_name = 'matching_app'

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('matching_app/', include('matching_app.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create_matching_room/', views.create_matching_room, name='create_matching_room'),
    path('list_matching_rooms/', views.list_matching_rooms, name='list_matching_rooms'),
    path('participate/<int:matching_room_id>/', views.participate, name='participate'),
    path('map/<int:matching_room_id>/', views.show_map, name='show_map'),
    path('chat/<int:matching_room_id>/', views.chat, name='chat'),
    #path('chatting/<int:matching_room_id>/', views.chatting, name='chatting'),
]


