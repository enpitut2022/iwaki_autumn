# Generated by Django 3.2 on 2023-01-11 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yarukikkake', '0011_lineuser_day_broadcast'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lineuser',
            name='day_broadcast',
        ),
        migrations.CreateModel(
            name='DayBroadcast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_broadcast', models.DateTimeField(blank=True, null=True, verbose_name='ブロードキャスト時間')),
                ('line_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='yarukikkake.lineuser', verbose_name='LINEユーザー')),
            ],
        ),
    ]