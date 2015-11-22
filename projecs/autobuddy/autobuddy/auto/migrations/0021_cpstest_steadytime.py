# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0020_udptest'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpstest',
            name='steadyTime',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
    ]
