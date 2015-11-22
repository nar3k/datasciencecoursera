# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0002_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='chassisConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('ip', models.GenericIPAddressField(protocol=b'IPv4')),
                ('card', models.IntegerField(default=1)),
                ('port1', models.IntegerField()),
                ('port2', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='neighborhoodConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('configPart', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='test',
            name='chassis',
            field=models.ForeignKey(default=1, to='auto.chassisConfig'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='test',
            name='dutProfile',
            field=models.CharField(default=b'BreakingPoint Default', max_length=128),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='test',
            name='neighborhood',
            field=models.ForeignKey(default=1, to='auto.neighborhoodConfig'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testconfig',
            name='chassisMode',
            field=models.CharField(default=b'setCardModeBPS', max_length=128, choices=[(b'setCardModeBPS_L23', b'L3'), (b'setCardModeBPS', b'L4')]),
            preserve_default=True,
        ),
    ]
