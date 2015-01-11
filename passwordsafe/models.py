from django.db import models

from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    owners = models.ManyToManyField(User)

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
    port = models.IntegerField(blank=True)
    url = models.CharField(max_length=200, blank=True)
    private_key = models.TextField(blank=True)
    public_key = models.TextField(blank=True)

    project = models.ForeignKey(Project)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
