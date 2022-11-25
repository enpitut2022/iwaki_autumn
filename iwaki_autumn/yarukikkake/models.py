from django.db import models

class Subject(models.Model):
    internal_id = models.IntegerField(verbose_name="内部id", primary_key=True, default=0)
    code = models.CharField(verbose_name="科目番号", max_length=10, default="")
    name = models.CharField(verbose_name='講義名',blank=False, null=False, max_length=150)
    teachers =  models.TextField(verbose_name='教員名', blank=True, max_length=100, default="")
    subtype =  models.TextField(verbose_name='種類', blank=True, max_length=32, default="")
    schools = models.CharField(verbose_name="学群等", max_length=4, default="", blank=True)
    colleges = models.CharField(verbose_name="学類等", max_length=40, default="", blank=True)

    def __str__(self):
        return self.code + " " + self.name