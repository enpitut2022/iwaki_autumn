# Generated by Django 3.2 on 2022-12-28 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yarukikkake', '0006_auto_20221228_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.IntegerField(choices=[(1, '始めてない'), (2, '始めた')], default=1, verbose_name='状態'),
        ),
    ]