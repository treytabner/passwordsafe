# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import encrypted_fields.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Credential',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', encrypted_fields.fields.EncryptedCharField(max_length=200)),
                ('description', encrypted_fields.fields.EncryptedTextField(blank=True)),
                ('username', encrypted_fields.fields.EncryptedCharField(max_length=200, blank=True)),
                ('password', encrypted_fields.fields.EncryptedCharField(max_length=200, blank=True)),
                ('hostname', encrypted_fields.fields.EncryptedCharField(max_length=200, blank=True)),
                ('port', encrypted_fields.fields.EncryptedCharField(max_length=200, blank=True)),
                ('protocol', encrypted_fields.fields.EncryptedCharField(max_length=200, blank=True)),
                ('command', encrypted_fields.fields.EncryptedCharField(max_length=200, blank=True)),
                ('url', encrypted_fields.fields.EncryptedCharField(max_length=200, blank=True)),
                ('private_key', encrypted_fields.fields.EncryptedTextField(blank=True)),
                ('public_key', encrypted_fields.fields.EncryptedTextField(blank=True)),
                ('script', encrypted_fields.fields.EncryptedTextField(blank=True)),
                ('created_at', encrypted_fields.fields.EncryptedDateTimeField(auto_now_add=True)),
                ('updated_at', encrypted_fields.fields.EncryptedDateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', encrypted_fields.fields.EncryptedCharField(max_length=200)),
                ('url', encrypted_fields.fields.EncryptedCharField(max_length=200, blank=True)),
                ('description', encrypted_fields.fields.EncryptedTextField(blank=True)),
                ('created_at', encrypted_fields.fields.EncryptedDateTimeField(auto_now_add=True)),
                ('updated_at', encrypted_fields.fields.EncryptedDateTimeField(auto_now=True)),
                ('owners', models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='credential',
            name='project',
            field=models.ForeignKey(related_name='credentials', to='passwordsafe.Project'),
            preserve_default=True,
        ),
    ]
