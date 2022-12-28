# Generated by Django 3.2 on 2022-12-28 06:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('yarukikkake', '0008_alter_task_task_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='lineuser',
            name='latast_task_id',
            field=models.UUIDField(default=uuid.uuid4, null=True, verbose_name='タスクID'),
        ),
    ]
