# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0009_auto_20151121_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='chassisconfig',
            name='group',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='connectconfig',
            name='configPart',
            field=models.TextField(default=b'puts "Connecting to the chassis"\r\nset bps [bps::connect %ip %username %password]\r\n#test create a connection\r\nputs "Creating chassis object"\r\nset chassis1 [$bps getChassis]    \r\nset group %group\r\n$chassis1 %crdMode 1  \r\n#reserve ports\r\nputs "Reserving ports"\r\n$chassis1 reservePort %card %port1 -group %group\r\n$chassis1 reservePort %card %port2 -group %group'),
        ),
    ]
