# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0014_cpstest_neighborhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='config',
            field=models.ForeignKey(to='auto.cpsTest'),
        ),
    ]
