from django.contrib import admin

from .models import Subject, LineUser, UserSubject, Task

# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    fields = ["code", "name", "unit", "grade", "semester", "teachers", "subtype", "schools", "colleges"]

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'task_user', 'task_start_time','task_status')
    
admin.site.register(Subject, SubjectAdmin)
admin.site.register(LineUser)
admin.site.register(UserSubject)
admin.site.register(Task, TaskAdmin)