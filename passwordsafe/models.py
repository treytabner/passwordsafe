from django.db import models

from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    owners = models.ManyToManyField(User)

    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name


class Credential(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    hostname = models.CharField(max_length=200)
    port = models.IntegerField()
    url = models.CharField(max_length=400)
    private_key = models.TextField()
    public_key = models.TextField()

    project = models.ForeignKey(Project)

    created_at = models.DateTimeField(auto_now_add=False)
    updated_at = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.name
