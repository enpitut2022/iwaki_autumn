# Generated by Django 3.2 on 2022-12-14 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('code', models.CharField(max_length=7, primary_key=True, serialize=False, verbose_name='科目番号')),
                ('name', models.CharField(max_length=150, verbose_name='科目名')),
                ('unit', models.CharField(default='', max_length=10, verbose_name='単位数')),
                ('grade', models.CharField(default='', max_length=30, verbose_name='履修年次')),
                ('semester', models.CharField(default='', max_length=30, verbose_name='学期')),
                ('teachers', models.TextField(blank=True, default='', max_length=100, verbose_name='教員名')),
                ('overview', models.TextField(blank=True, default='', max_length=200, verbose_name='概要')),
                ('subtype', models.TextField(blank=True, default='', max_length=32, verbose_name='種類')),
                ('schools', models.CharField(blank=True, default='', max_length=40, verbose_name='学群等')),
                ('colleges', models.CharField(blank=True, default='', max_length=40, verbose_name='学類等')),
            ],
        ),
    ]
