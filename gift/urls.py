from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GiftViewSet, create_gift, send_gift
from . import views

router = DefaultRouter()
router.register(r'gifts', GiftViewSet)

urlpatterns = [
    # ...
    path('send/', create_gift, name='create_gift'),  # create_gift 뷰를 '/send/' URL에 추가
    path('api/', include(router.urls)),  # GiftViewSet의 API URL을 '/api/'에 추가
    path('create/', send_gift, name='send_gift'),
    path('success/', views.success_view, name='success'),
]
