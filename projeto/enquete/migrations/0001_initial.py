# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=40)),
                ('email', models.TextField()),
                ('HTML', models.CharField(max_length=1, null=True)),
                ('CSS', models.CharField(max_length=1, null=True)),
                ('Javascript', models.CharField(max_length=1, null=True)),
                ('Python', models.CharField(max_length=1, null=True)),
                ('Django', models.CharField(max_length=1, null=True)),
                ('Desenv_IOS', models.CharField(max_length=1, null=True)),
                ('Desenv_Android', models.CharField(max_length=1, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
