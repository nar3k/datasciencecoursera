# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0003_auto_20151121_0911'),
    ]

    operations = [
        migrations.AddField(
            model_name='chassisconfig',
            name='configPart',
            field=models.TextField(default='tle'),
            preserve_default=False,
        ),
    ]
