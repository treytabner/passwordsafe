from django.contrib.auth.models import User

from rest_framework import serializers

from passwordsafe.models import Project
from passwordsafe.models import Credential


class UserSerializer(serializers.HyperlinkedModelSerializer):
    projects = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='project-detail'
    )

    class Meta:
        model = User
        fields = ('url', 'username', 'is_superuser', 'email', 'projects')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    credentials = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='credential-detail'
    )

    class Meta:
        model = Project
        fields = ('url', 'name', 'description', 'owners',
                  'created_at', 'updated_at', 'credentials')


class CredentialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Credential
