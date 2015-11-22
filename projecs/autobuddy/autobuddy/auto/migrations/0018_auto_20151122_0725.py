# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0017_remove_cpstest_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='device',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='result',
            name='software',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='result',
            name='type',
            field=models.CharField(max_length=128, null=True),
            preserve_default=True,
        ),
    ]
