# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0013_auto_20151121_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='cpstest',
            name='neighborhood',
            field=models.ForeignKey(default=1, to='auto.neighborhoodConfig'),
            preserve_default=False,
        ),
    ]
