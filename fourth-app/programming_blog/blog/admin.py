from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms
from .models import *


class BlogAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Blog
        fields = '__all__'


class BlogAdmin(admin.ModelAdmin):
    form = BlogAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'cat', 'time_completed', 'photo', 'id_published',)
    list_display_links = ('id', 'title',)
    search_fields = ('title', 'content')
    list_editable = ('id_published',)
    list_filter = ('id_published', 'time_completed',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_header = 'Админ-панель блога'
admin.site.site_title = 'Админ-панель блога'