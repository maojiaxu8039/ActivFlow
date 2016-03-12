# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-06 09:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('core', '0002_auto_20160306_0831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assignee',
        ),
        migrations.AddField(
            model_name='task',
            name='role',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='assignedtasks', to='auth.Group'),
            preserve_default=False,
        ),
    ]
