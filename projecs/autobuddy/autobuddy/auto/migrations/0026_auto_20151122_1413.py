# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0025_auto_20151122_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='httpTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('tputMAX', models.IntegerField(default=100)),
                ('failSTEP', models.IntegerField(default=50)),
                ('steadyTime', models.IntegerField(default=1)),
                ('configfields', models.CharField(default=b'tputMAX failSTEP steadyTime dutprofile', max_length=300)),
                ('dutprofile', models.CharField(max_length=128)),
                ('resultkey', models.CharField(default=b'rsp:.+', max_length=128)),
                ('config', models.ForeignKey(to='auto.Template')),
                ('neighborhood', models.ForeignKey(to='auto.neighborhoodConfig')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cctest',
            name='dutprofile',
            field=models.CharField(default='SRX', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cpstest',
            name='dutprofile',
            field=models.CharField(default='SRX', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tpstest',
            name='dutprofile',
            field=models.CharField(default='SRX', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='udptest',
            name='dutprofile',
            field=models.CharField(default='SRX', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cctest',
            name='configfields',
            field=models.CharField(default=b'rateMAX steadyTime failSTEP rateMAX steadyTime failSTEP dutprofile', max_length=300),
        ),
        migrations.AlterField(
            model_name='cpstest',
            name='configfields',
            field=models.CharField(default=b'cpsMAX cpsSTEP failSTEP neighborhood failSTEP dutprofile', max_length=300),
        ),
        migrations.AlterField(
            model_name='tpstest',
            name='configfields',
            field=models.CharField(default=b'tpsMAX tpsSTEP tputMAX steadyTime failSTEP neighborhood modifier dutprofile', max_length=300),
        ),
        migrations.AlterField(
            model_name='udptest',
            name='configfields',
            field=models.CharField(default=b'allowedDrop steadyTime tputSTEP tputMAX packetSizelist dutprofile', max_length=300),
        ),
    ]
