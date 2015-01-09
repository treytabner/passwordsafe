from django.contrib import admin

from passwordsafe.models import Project, Credential


admin.site.register(Project)
admin.site.register(Credential)
