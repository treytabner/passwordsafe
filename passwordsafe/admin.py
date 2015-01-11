from django.contrib import admin

from passwordsafe.models import Project
from passwordsafe.models import Credential


admin.site.register(Project)
admin.site.register(Credential)
