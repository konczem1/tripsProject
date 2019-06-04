from rest_framework import viewsets
from .serializers import UserSerializer, PhotoSerializer
from .models import User, Photo


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users info to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users info to be viewed or edited.
    """
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
