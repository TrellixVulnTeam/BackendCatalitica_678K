# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ingenieria', '0004_auto_20170215_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='datosventa',
            name='AyudanteC',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=19),
        ),
        migrations.AddField(
            model_name='datosventa',
            name='IngenieroAC',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=19),
        ),
        migrations.AddField(
            model_name='datosventa',
            name='TecnicoAC',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=19),
        ),
        migrations.AddField(
            model_name='datosventa',
            name='TecnicoBC',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=19),
        ),
    ]