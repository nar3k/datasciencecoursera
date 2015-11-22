# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0008_auto_20151121_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testconfig',
            name='chassisMode',
        ),
        migrations.AddField(
            model_name='chassisconfig',
            name='chassisMode',
            field=models.CharField(default=b'setCardModeBPS', max_length=128, choices=[(b'setCardModeBPS_L23', b'L3'), (b'setCardModeBPS', b'L4')]),
            preserve_default=True,
        ),
    ]
