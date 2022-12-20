from django.contrib import admin

from .models import Subject, LineUser, UserSubject

# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    fields = ["code", "name", "unit", "grade", "semester", "teachers", "subtype", "schools", "colleges"]
    
admin.site.register(Subject, SubjectAdmin)
admin.site.register(LineUser)
admin.site.register(UserSubject)