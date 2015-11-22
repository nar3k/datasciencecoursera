# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0018_auto_20151122_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='status',
            field=models.CharField(default=b'N', max_length=128, choices=[(b'A', b'Active'), (b'P', b'Passed'), (b'F', b'Failed'), (b'N', b'Not started')]),
            preserve_default=True,
        ),
    ]
