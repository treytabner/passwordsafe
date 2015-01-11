from django.contrib.auth.models import User, Group
from rest_framework import serializers
from passwordsafe.models import Project, Credential


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        #fields = ('url', 'username', 'email', 'groups')


class CredentialSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Credential
        #fields = ('url', 'username', 'email', 'groups')

