from .serializers import UserDetailsSerializer
from django.conf import settings
from django.shortcuts import get_object_or_404
from .models import User
from rest_framework import viewsets
from .permissions import IsOwner


class UserViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Users.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    permission_classes = []
