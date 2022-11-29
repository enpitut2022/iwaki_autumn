from django.contrib import admin

from .models import Subject

# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    fields = ["code", "name", "unit", "grade", "semester", "teachers", "subtype", "schools", "colleges"]
    
admin.site.register(Subject, SubjectAdmin)