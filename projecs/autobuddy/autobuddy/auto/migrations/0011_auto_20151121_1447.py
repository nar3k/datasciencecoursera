# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0010_auto_20151121_1444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chassisconfig',
            old_name='chassisMode',
            new_name='crdMode',
        ),
    ]
