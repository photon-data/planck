from django.contrib import admin
from .models.VersionControlType import  VersionControlType
from .models.VersionControl import  VersionControl

# Registering the models
admin.site.register(VersionControl)
admin.site.register(VersionControlType)
# Register your models here.
