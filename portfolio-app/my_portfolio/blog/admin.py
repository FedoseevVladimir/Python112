from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import *


class MyblogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Myblog
        fields = '__all__'


class MyblogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = MyblogAdminForm


admin.site.register(Blog)
admin.site.register(Myblog, MyblogAdmin)

admin.site.site_header = 'Админ-панель блога'
admin.site.site_title = 'Админ-панель блога'