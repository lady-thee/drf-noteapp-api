from django.contrib import admin
from .models import Notes



class AdminManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'body', 'created']


admin.site.register(Notes, AdminManager)
