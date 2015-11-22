# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0021_cpstest_steadytime'),
    ]

    operations = [
        migrations.CreateModel(
            name='ccTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('steadyTime', models.IntegerField(default=1)),
                ('rateMAX', models.IntegerField(default=2000)),
                ('failSTEP', models.IntegerField(default=50)),
                ('config', models.ForeignKey(to='auto.Template')),
                ('neighborhood', models.ForeignKey(to='auto.neighborhoodConfig')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
