# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-22 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potato', '0003_auto_20190521_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Возраст'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='Информация о себе'),
        ),
    ]