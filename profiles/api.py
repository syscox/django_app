from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer
from .serializers import ProfileAddressSerializer, ProfileUserSerializer, ProfileMediaSerializer
from .models import User as UserP, Address, Media


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProfileUserViewSet(viewsets.ModelViewSet):
    queryset = UserP.objects.all().order_by('-id')
    serializer_class = ProfileUserSerializer


class ProfileAddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = ProfileAddressSerializer


class ProfileMediaViewSet(viewsets.ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = ProfileMediaSerializer
