# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0012_auto_20151121_1540'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpstest',
            name='config',
            field=models.ForeignKey(default=1, to='auto.Template'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cpstest',
            name='cpsMAX',
            field=models.IntegerField(default=5000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cpstest',
            name='cpsSTEP',
            field=models.IntegerField(default=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cpstest',
            name='failSTEP',
            field=models.IntegerField(default=50),
            preserve_default=True,
        ),
    ]
