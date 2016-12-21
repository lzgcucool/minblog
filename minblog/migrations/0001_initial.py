# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='标题')),
                ('link', models.CharField(max_length=150, verbose_name='链接')),
                ('content', models.TextField(verbose_name='内容')),
                ('snippet', models.CharField(max_length=300, verbose_name='摘要')),
                ('pubtime', models.DateTimeField(verbose_name='发布时间')),
            ],
        ),
        migrations.CreateModel(
            name='PostTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标签名')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='posttags',
            field=models.ManyToManyField(to='minblog.PostTags', verbose_name='文章标签'),
        ),
    ]
