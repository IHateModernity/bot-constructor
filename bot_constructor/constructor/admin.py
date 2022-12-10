from django.contrib import admin
from .models import Command

class CommandAdmin(admin.ModelAdmin):
    list_display = ('creating_date',)


admin.site.register(Command, CommandAdmin)
