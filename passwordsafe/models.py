from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    owners = models.ManyToManyField(User, blank=False, null=False,
                                    related_name='projects')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Credential(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    username = models.CharField(max_length=200, blank=True)
    password = models.CharField(max_length=200, blank=True)
    hostname = models.CharField(max_length=200, blank=True)
    port = models.CharField(max_length=200, blank=True)
    protocol = models.CharField(max_length=200, blank=True)
    command = models.CharField(max_length=200, blank=True)
    uri = models.CharField(max_length=200, blank=True)
    private_key = models.TextField(blank=True)
    public_key = models.TextField(blank=True)
    script = models.TextField(blank=True)

    project = models.ForeignKey(Project, blank=False, null=False,
                                related_name='credentials')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
