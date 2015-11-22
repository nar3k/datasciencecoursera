# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0005_auto_20151121_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chassisconfig',
            name='configPart',
            field=models.TextField(default=b'puts "Connecting to the chassis"\r\nset bps [bps::connect $ip $username $password]\r\n#test create a connection\r\nputs "Creating chassis object"\r\nset chassis1 [$bps getChassis]    \r\nset group $group\r\n$chassis1 $cardMode 1  \r\n#reserve ports\r\nputs "Reserving ports"\r\n$chassis1 reservePort $card $port1 -group $group\r\n$chassis1 reservePort $card $port2 -group $group'),
        ),
    ]
