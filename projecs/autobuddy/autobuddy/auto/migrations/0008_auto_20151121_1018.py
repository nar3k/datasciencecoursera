# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0007_auto_20151121_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chassisconfig',
            name='port1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='chassisconfig',
            name='port2',
            field=models.IntegerField(default=4),
        ),
    ]
