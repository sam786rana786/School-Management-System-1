# Generated by Django 2.2.2 on 2019-06-19 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_remove_subjects_department_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersdb',
            name='role',
        ),
        migrations.RemoveField(
            model_name='usersdb',
            name='username',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='usersdb',
        ),
    ]
