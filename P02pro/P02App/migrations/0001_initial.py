# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EMP',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('sname', models.CharField(max_length=20)),
                ('sal', models.IntegerField()),
            ],
        ),
    ]
