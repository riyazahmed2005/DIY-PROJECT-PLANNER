# diy/admin.py
from django.contrib import admin
from .models import DIYProject

@admin.register(DIYProject)
class DIYProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'materials')
    search_fields = ('name', 'description')
