# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0004_chassisconfig_configpart'),
    ]

    operations = [
        migrations.AddField(
            model_name='chassisconfig',
            name='password',
            field=models.CharField(default=b'admin', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chassisconfig',
            name='username',
            field=models.CharField(default=b'admin', max_length=128),
            preserve_default=True,
        ),
    ]
