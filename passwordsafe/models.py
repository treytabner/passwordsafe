from django.db import models
from django.contrib.auth.models import User

from encrypted_fields import EncryptedCharField
from encrypted_fields import EncryptedTextField
from encrypted_fields import EncryptedDateTimeField


class Project(models.Model):
    name = EncryptedCharField(max_length=200)
    url = EncryptedCharField(max_length=200, blank=True)
    description = EncryptedTextField(blank=True)

    owners = models.ManyToManyField(User, blank=False, null=False,
                                    related_name='projects')

    created_at = EncryptedDateTimeField(auto_now_add=True)
    updated_at = EncryptedDateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Credential(models.Model):
    name = EncryptedCharField(max_length=200)
    description = EncryptedTextField(blank=True)
    username = EncryptedCharField(max_length=200, blank=True)
    password = EncryptedCharField(max_length=200, blank=True)
    hostname = EncryptedCharField(max_length=200, blank=True)
    port = EncryptedCharField(max_length=200, blank=True)
    protocol = EncryptedCharField(max_length=200, blank=True)
    command = EncryptedCharField(max_length=200, blank=True)
    url = EncryptedCharField(max_length=200, blank=True)
    private_key = EncryptedTextField(blank=True)
    public_key = EncryptedTextField(blank=True)
    script = EncryptedTextField(blank=True)

    project = models.ForeignKey(Project, blank=False, null=False,
                                related_name='credentials')

    created_at = EncryptedDateTimeField(auto_now_add=True)
    updated_at = EncryptedDateTimeField(auto_now=True)

    def __str__(self):
        return self.name
