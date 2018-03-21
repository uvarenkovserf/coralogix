from django.contrib import admin

from .models import LogsBuffer


@admin.register(LogsBuffer)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['level', 'log']
