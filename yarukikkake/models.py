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
    day_of_week = models.CharField(verbose_name="曜日",blank=False, null=False, default="", max_length=20)
    teachers =  models.TextField(verbose_name='教員名', blank=True, max_length=100, default="")
    overview = models.TextField(verbose_name='概要', blank=True, max_length=200, default="")
    subtype =  models.TextField(verbose_name='種類', blank=True, max_length=32, default="")
    schools = models.CharField(verbose_name="学群等", blank=True,max_length=40, default="")
    colleges = models.CharField(verbose_name="学類等", blank=True, max_length=40, default="")

    def __str__(self):
        return self.code + " " + self.name

class LineUser(models.Model):
    user_id = models.CharField('ユーザーID', max_length=100, unique=True)
    display_name = models.CharField('表示名', max_length=255)

    def __str__(self):
        return self.display_name

class UserSubject(models.Model):
    push = models.ForeignKey(LineUser, verbose_name='LINEユーザー', on_delete=models.SET_NULL, blank=True, null=True)
    subject = models.TextField('科目名')
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return f'{self.push} - {self.text[:10]} - {self.is_admin}'