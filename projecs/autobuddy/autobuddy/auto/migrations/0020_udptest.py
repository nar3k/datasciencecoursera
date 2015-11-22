# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0019_result_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='udpTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('allowedDrop', models.FloatField(default=0.3)),
                ('steadyTime', models.IntegerField(default=1)),
                ('tputMAX', models.IntegerField(default=1000)),
                ('tputSTEP', models.IntegerField(default=1)),
                ('packetSizelist', models.CharField(default=b'64 128 256 512 1024 1500', max_length=300)),
                ('config', models.ForeignKey(to='auto.Template')),
                ('neighborhood', models.ForeignKey(to='auto.neighborhoodConfig')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
