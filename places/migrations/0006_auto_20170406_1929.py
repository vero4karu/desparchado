# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 00:29
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_auto_20170311_1843'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AddField(
            model_name='place',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='place',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.City', verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Nombre'),
        ),
    ]
