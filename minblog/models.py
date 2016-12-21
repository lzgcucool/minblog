from django.db import models

# Create your models here.


class PostTags(models.Model):
	name = models.CharField('标签名', max_length=20)
	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField('标题', max_length=120)
	link = models.CharField('链接', max_length=150)
	content = models.TextField('内容')
	snippet = models.CharField('摘要', max_length=300)
	posttags = models.ManyToManyField(PostTags, verbose_name='文章标签')
	pubtime = models.DateTimeField('发布时间')

	def __str__(self):
		return self. title

	class Meta:
		ordering = ['-pubtime']