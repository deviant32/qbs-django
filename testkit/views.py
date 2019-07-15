from .serializers import TestKitSerializer
from .models import TestKit
from rest_framework import viewsets


class TestKitViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing test kits.
    """
    queryset = TestKit.objects.all()
    serializer_class = TestKitSerializer
