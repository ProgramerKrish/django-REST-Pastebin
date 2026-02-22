from django.shortcuts import render
from django.contrib.auth.models import Group,User
from rest_framework import permissions, viewsets

from restquickstart.serializers import GroupSerializer,UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    "API endpoint lets user to view|modify"

    queryset=User.objects.all().order_by("date_joined")
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    "API endpoint lets groups to be viwed"

    queryset=Group.objects.all().order_by("name")
    serializer_class=GroupSerializer
    permission_classes=[permissions.IsAuthenticated]
