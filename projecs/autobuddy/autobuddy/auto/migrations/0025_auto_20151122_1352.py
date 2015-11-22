# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0024_auto_20151122_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='tpstest',
            name='modifier',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tpstest',
            name='configfields',
            field=models.CharField(default=b'tpsMAX tpsSTEP tputMAX steadyTime failSTEP neighborhood modifier', max_length=300),
        ),
    ]
