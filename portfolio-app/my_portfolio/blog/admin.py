from django.contrib import admin
from .models import *


class MyblogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Blog)
admin.site.register(Myblog, MyblogAdmin)
