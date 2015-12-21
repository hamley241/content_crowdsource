# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sticker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('category', models.CharField(max_length=20)),
                ('like', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'date added')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('theme', models.CharField(default=b'NA', max_length=20)),
                ('lang', models.CharField(default=b'NA', max_length=20)),
                ('sticker', models.ForeignKey(to='tagsource.Sticker')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='sticker',
            unique_together=set([('name', 'category')]),
        ),
    ]
