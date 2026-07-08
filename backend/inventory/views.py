from rest_framework import viewsets
from .models import TextileWaste
from .serializers import TextileWasteSerializer


class TextileWasteViewSet(viewsets.ModelViewSet):
    queryset = TextileWaste.objects.all()
    serializer_class = TextileWasteSerializer
