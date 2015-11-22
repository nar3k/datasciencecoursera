# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0022_cctest'),
    ]

    operations = [
        migrations.AddField(
            model_name='cctest',
            name='resultkey',
            field=models.CharField(default=b'MAX_CC:.+', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cpstest',
            name='resultkey',
            field=models.CharField(default=b'MAX_CPS:.+', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='udptest',
            name='resultkey',
            field=models.CharField(default=b'pkt:.+', max_length=128),
            preserve_default=True,
        ),
    ]
