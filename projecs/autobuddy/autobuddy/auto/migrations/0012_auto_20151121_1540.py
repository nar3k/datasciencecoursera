# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0011_auto_20151121_1447'),
    ]

    operations = [
        migrations.CreateModel(
            name='cpsTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'default', unique=True, max_length=128)),
                ('configPart', models.TextField(default=b'puts "Connecting to the chassis"\r\nset bps [bps::connect %ip %username %password]\r\n#test create a connection\r\nputs "Creating chassis object"\r\nset chassis1 [$bps getChassis]    \r\nset group %group\r\n$chassis1 %crdMode %card  \r\n#reserve ports\r\nputs "Reserving ports"\r\n$chassis1 reservePort %card %port1 -group %group\r\n$chassis1 reservePort %card %port2 -group %group')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='chassisconfig',
            name='config',
            field=models.ForeignKey(to='auto.Template'),
        ),
        migrations.DeleteModel(
            name='connectConfig',
        ),
    ]
