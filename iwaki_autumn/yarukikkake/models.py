from concurrent.futures import thread
from django.db import models
from django.utils import timezone
import uuid

class Subject(models.Model):
    code = models.CharField(verbose_name="科目番号", max_length=7, primary_key=True)
    name = models.CharField(verbose_name='科目名',blank=False, null=False, max_length=150)
    unit = models.CharField(verbose_name="単位数",blank=False, null=False, default="", max_length=10)
    grade = models.CharField(verbose_name="履修年次",blank=False, null=False, default="", max_length=30)
    semester = models.CharField(verbose_name="学期",blank=False, null=False, default="", max_length=30)
    teachers =  models.TextField(verbose_name='教員名', blank=True, max_length=100, default="")
    overview = models.TextField(verbose_name='概要', blank=True, max_length=200, default="")
    subtype =  models.TextField(verbose_name='種類', blank=True, max_length=32, default="")
    schools = models.CharField(verbose_name="学群等", blank=True,max_length=40, default="")
    colleges = models.CharField(verbose_name="学類等", blank=True, max_length=40, default="")

    def __str__(self):
        return self.code + " " + self.name


