from django.contrib import admin
from .models import *


class AdminServices(admin.ModelAdmin):

    list_display = ['title', 'content', 'status']
    list_filter = ['status']
    search_fields = ['title']

admin.site.register(Products)
admin.site.register(Category)