# Generated by Django 3.2 on 2022-12-16 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yarukikkake', '0002_linemessage_lineuser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LineMessage',
            new_name='UserSubject',
        ),
    ]