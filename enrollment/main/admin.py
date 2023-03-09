from django.contrib import admin

# Register your models here.

from . models import Hospitalization, Visit2

admin.site.register(Hospitalization)
admin.site.register(Visit2)