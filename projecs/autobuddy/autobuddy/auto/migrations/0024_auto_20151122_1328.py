# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0023_auto_20151122_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='tpsTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('tpsMAX', models.IntegerField(default=10000)),
                ('tpsSTEP', models.IntegerField(default=100)),
                ('failSTEP', models.IntegerField(default=100)),
                ('tputMAX', models.IntegerField(default=1000)),
                ('steadyTime', models.IntegerField(default=1)),
                ('configfields', models.CharField(default=b'tpsMAX tpsSTEP tputMAX failSTEP neighborhood failSTEP', max_length=300)),
                ('resultkey', models.CharField(default=b'MAX_TPS:.+', max_length=128)),
                ('config', models.ForeignKey(to='auto.Template')),
                ('neighborhood', models.ForeignKey(to='auto.neighborhoodConfig')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cctest',
            name='configfields',
            field=models.CharField(default=b'rateMAX steadyTime failSTEP rateMAX steadyTime failSTEP', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='chassisconfig',
            name='configfields',
            field=models.CharField(default=b'card crdMode config ip name password port1 port2 username group', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cpstest',
            name='configfields',
            field=models.CharField(default=b'cpsMAX cpsSTEP failSTEP neighborhood failSTEP', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='neighborhoodconfig',
            name='configfields',
            field=models.CharField(default=b'name', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='udptest',
            name='configfields',
            field=models.CharField(default=b'allowedDrop steadyTime tputSTEP tputMAX packetSizelist', max_length=300),
            preserve_default=True,
        ),
    ]
