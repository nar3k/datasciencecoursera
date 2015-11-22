# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0006_auto_20151121_1005'),
    ]

    operations = [
        migrations.CreateModel(
            name='connectConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'default', unique=True, max_length=128)),
                ('configPart', models.TextField(default=b'puts "Connecting to the chassis"\r\nset bps [bps::connect $ip $username $password]\r\n#test create a connection\r\nputs "Creating chassis object"\r\nset chassis1 [$bps getChassis]    \r\nset group $group\r\n$chassis1 $cardMode 1  \r\n#reserve ports\r\nputs "Reserving ports"\r\n$chassis1 reservePort $card $port1 -group $group\r\n$chassis1 reservePort $card $port2 -group $group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='chassisconfig',
            name='configPart',
        ),
        migrations.AddField(
            model_name='chassisconfig',
            name='config',
            field=models.ForeignKey(default=1, to='auto.connectConfig'),
            preserve_default=False,
        ),
    ]
