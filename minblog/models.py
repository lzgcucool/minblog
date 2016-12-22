#-*-coding:utf-8 -*-
from django.db import models

# Create your models here.


class PostTags(models.Model):
	name = models.CharField(u'标签名', max_length=20)
	def __unicode__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(u'标题', max_length=120)
	link = models.CharField(u'链接', max_length=150)
	content = models.TextField(u'内容')
	snippet = models.CharField(u'摘要', max_length=300)
	posttags = models.ManyToManyField(PostTags, verbose_name=u'文章标签')
	pubtime = models.DateTimeField(u'发布时间')

	def __unicode__(self):
		return self. title

	class Meta:
		ordering = ['-pubtime']
