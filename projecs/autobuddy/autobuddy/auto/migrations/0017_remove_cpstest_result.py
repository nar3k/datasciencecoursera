# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0016_auto_20151121_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cpstest',
            name='result',
        ),
    ]
