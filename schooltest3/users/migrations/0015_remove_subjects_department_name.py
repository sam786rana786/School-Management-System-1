# Generated by Django 2.2.2 on 2019-06-19 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20190619_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='department_name',
        ),
    ]
