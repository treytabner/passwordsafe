from django.contrib.auth.models import User
from rest_framework import viewsets

from passwordsafe.serializers import UserSerializer
from passwordsafe.serializers import ProjectSerializer
from passwordsafe.serializers import CredentialSerializer

from passwordsafe.models import Project
from passwordsafe.models import Credential


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated():
            if user.is_superuser:
                return self.queryset
            else:
                return User.objects.filter(id=user.id)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated():
            if user.is_superuser:
                return self.queryset
            else:
                return Project.objects.filter(owners=user)


class CredentialViewSet(viewsets.ModelViewSet):
    queryset = Credential.objects.all()
    serializer_class = CredentialSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated():
            if user.is_superuser:
                return self.queryset
            else:
                return Credential.objects.filter(project__owners=user)
