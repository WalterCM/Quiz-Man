# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_auto_20170322_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.CharField(max_length=600),
        ),
    ]
