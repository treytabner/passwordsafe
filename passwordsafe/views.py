from django.contrib.auth.models import User
from rest_framework import viewsets

from passwordsafe.serializers import UserSerializer
from passwordsafe.serializers import ProjectSerializer
from passwordsafe.serializers import CredentialSerializer

from passwordsafe.models import Project
from passwordsafe.models import Credential


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CredentialViewSet(viewsets.ModelViewSet):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer
