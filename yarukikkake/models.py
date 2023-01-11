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
    day_of_week = models.CharField(verbose_name="曜日",blank=False, null=False, default="", max_length=100)
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
    state = models.IntegerField('状態', default=1) # 1 == ユーザー名登録・追加, 2 == タスク名登録, 3 == タスク開始時刻登録, 4 == タスク開始報告, 5 == タスク確認
    latast_task_id = models.UUIDField('タスクID', default=uuid.uuid4, editable=True, unique=False, null=True)
    def __str__(self):
        return self.display_name

class DayBroadcast(models.Model):
    line_user = models.ForeignKey(LineUser, verbose_name='LINEユーザー', on_delete=models.CASCADE, blank=True, null=True)
    day_broadcast = models.DateTimeField('ブロードキャスト時間', blank=True, null=True) # その日に何回送られたかをチェックする用
    def __str__(self) -> str:
        return self.line_user.display_name + str(self.day_broadcast)
    
class UserSubject(models.Model):
    push = models.ForeignKey(LineUser, verbose_name='LINEユーザー', on_delete=models.CASCADE, blank=True, null=True)
    subject = models.ForeignKey(Subject, verbose_name='対応科目', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField('作成日', default=timezone.now)

    def __str__(self):
        return self.push.display_name + " " + self.subject.name
    
class LineGroup(models.Model):
    group_id = models.CharField('グループID', max_length=100, unique=True)
    def __str__(self):
        return self.group_id

class Task(models.Model):
    STATE = (
        (1, '始めてない'),
        (2, '始めた'),
    )
    task_id = models.UUIDField('タスクID', default=uuid.uuid4, editable=False, unique=True)
    task_name = models.CharField(verbose_name='タスク名', blank=False, null=False, max_length=30)
    task_user = models.ForeignKey(LineUser, verbose_name='LINEユーザー', on_delete=models.CASCADE, blank=True, null=True)
    task_group = models.ForeignKey(LineGroup, verbose_name='LINEグループ', on_delete=models.CASCADE, blank=True, null=True)
    task_start_time = models.DateTimeField("タスク開始時刻", null=True)
    task_status = models.IntegerField('状態', choices=STATE,default=1) # 1 == 始めてない, 2 == 始めた

    def __str__(self):
        return self.task_name + " " + str(self.task_start_time) + " " + str(self.task_status)