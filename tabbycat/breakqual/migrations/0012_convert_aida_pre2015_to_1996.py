# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 11:33
from __future__ import unicode_literals

from django.db import migrations


def rename_aida_pre2015_to_1996(apps, schema_editor):
    BreakCategory = apps.get_model("breakqual", "BreakCategory")
    for category in BreakCategory.objects.all():
        if category.rule == 'aida-pre2015':
            category.rule = 'aida-1996'
            category.save()


def rename_aida_1996_to_pre2015(apps, schema_editor):
    BreakCategory = apps.get_model("breakqual", "BreakCategory")
    for category in BreakCategory.objects.all():
        if category.rule == 'aida-1996':
            category.rule = 'aida-pre2015'
            category.save()


class Migration(migrations.Migration):

    dependencies = [
        ('breakqual', '0011_rename_aida_pre2015_to_1996'),
    ]

    operations = [
        migrations.RunPython(rename_aida_pre2015_to_1996, reverse_code=rename_aida_1996_to_pre2015),
    ]