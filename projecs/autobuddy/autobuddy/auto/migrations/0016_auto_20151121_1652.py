# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auto', '0015_auto_20151121_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('result', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='test',
            name='chassis',
        ),
        migrations.RemoveField(
            model_name='test',
            name='config',
        ),
        migrations.RemoveField(
            model_name='test',
            name='neighborhood',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
        migrations.AddField(
            model_name='cpstest',
            name='result',
            field=models.ForeignKey(default=1, to='auto.Result'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='template',
            name='configPart',
            field=models.TextField(default=b'COPY TCL TEMPLATE HERE'),
        ),
    ]
