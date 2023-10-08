from rest_framework import viewsets, status
from .models import Gift, User
from .serializers import GiftSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class GiftViewSet(viewsets.ModelViewSet):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer