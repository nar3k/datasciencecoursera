# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0026_auto_20151122_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cctest',
            name='dutprofile',
            field=models.CharField(default=b'BreakingPoint Default', max_length=128),
        ),
        migrations.AlterField(
            model_name='cpstest',
            name='dutprofile',
            field=models.CharField(default=b'BreakingPoint Default', max_length=128),
        ),
        migrations.AlterField(
            model_name='httptest',
            name='dutprofile',
            field=models.CharField(default=b'BreakingPoint Default', max_length=128),
        ),
        migrations.AlterField(
            model_name='tpstest',
            name='dutprofile',
            field=models.CharField(default=b'BreakingPoint Default', max_length=128),
        ),
        migrations.AlterField(
            model_name='udptest',
            name='dutprofile',
            field=models.CharField(default=b'BreakingPoint Default', max_length=128),
        ),
    ]
