from rest_framework import viewsets
from .models import Gift
from .serializers import GiftSerializer

class GiftViewSet(viewsets.ModelViewSet):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer