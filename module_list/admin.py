from module_list.models import Module
from django.contrib import admin

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'updated')
    list_filter = ['updated']
    ordering = ['-updated']

admin.site.register(Module, ModuleAdmin)
