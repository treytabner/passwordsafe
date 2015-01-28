from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.settings import api_settings

from passwordsafe.models import Project
from passwordsafe.models import Credential


api_settings.URL_FIELD_NAME = 'self'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('self', 'username', 'is_superuser', 'email', 'projects')
        depth = 1


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('self', 'name', 'url', 'description', 'owners',
                  'created_at', 'updated_at', 'credentials')
        depth = 1


class OwnedProjectValidator:
    def set_context(self, serializer_field):
        self.user = serializer_field.context['request'].user

    def __call__(self, credential):
        project = credential.get('project')
        if self.user not in project.owners.all():
            message = 'Project must be owned by user.'
            raise serializers.ValidationError(message)


class CredentialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Credential
        validators = [
            OwnedProjectValidator()
        ]
        depth = 1
