# *-* coding:utf-8 *-*
# file: views.py
import sys
import markdown2
from django.views.generic import TemplateView, ListView, DetailView
from django.conf import settings
from django.http import Http404
from .models import Post, PostTags
reload(sys)
sys.setdefaultencoding('utf8')


class BaseMixin(object):
	""" public resource load object """
	def get_context_data(self, *arg, **kwargs):
		context = super(BaseMixin, self).get_context_data(**kwargs)
		context['website_title'] = settings.SITE_TITLE
		context['tags'] = PostTags.objects.all()[:30]
		context['date_archive'] = Post.objects.datetimes('pubtime', 'month', order='DESC')
		return context

class AboutView(BaseMixin, TemplateView):
	template_name = 'about.html'

	def get_context_data(self, *arg, **kwargs):
		context = super(AboutView, self).get_context_data(**kwargs)
		context['subtitle'] = '关于我 - '
		return context

class IndexView(BaseMixin, ListView):
	template_name = 'index.html'
	context_object_name = 'post_list'
	paginate_by = settings.PAGE_NUM

	def check_args(self):
		try:
			tag = self.kwargs['tag']
		except KeyError:
			tag = None
		try:
			arch_year = self.kwargs['arch_year']
			arch_month = self.kwargs['arch_month']
		except KeyError:
			arch_year = None
			arch_month = None
		return (tag, arch_year, arch_month)

	def get_queryset(self):
		tag, arch_year, arch_month = self.check_args()
		if tag is not None:
			post_list = Post.objects.filter(posttags__name=tag)
		elif arch_year and arch_month:
			search_arch = {}
			search_arch['pubtime__year'], search_arch['pubtime__month'] = arch_year, arch_month
			post_list = Post.objects.filter(**search_arch)
		else:
			post_list = Post.objects.all()
		return post_list
	def get_context_data(self, *arg, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		tag, arch_year, arch_month = self.check_args()
		context['istag'], context['isarch'], context['isindex'] = None, None, None
		if tag:
			context['tagname'] = tag
			context['subtitle'] = "%s - 标签 - " % context['tagname'] 
			context['istag'] = True
		elif arch_year and arch_month:
			context['archtime'] = "%s年%s月" % (arch_year, arch_month) 
			context['subtitle'] = "%s归档 - " % context['archtime']
			context['isarch'] = True
		else:
			context['isindex'] = True

		return context

class PostDetail(BaseMixin, DetailView):
	queryset = Post.objects.all()
	template_name = 'content.html'
	context_object_name = 'post_detail'
	slug_field = 'link'

	def get_object(self, queryset=None):
		obj = super(PostDetail, self).get_object()
		obj.content = markdown2.markdown(obj.content, extras=['fenced-code-blocks'],)
		return obj

	def get(self, request, *args, **kwargs):
		return super(PostDetail, self).get(request, *args, **kwargs)

	def get_context_data(self, *arg, **kwargs):
		context = super(PostDetail, self).get_context_data(**kwargs)
		post_detail = self.get_object()
		context['subtitle'] = '%s - ' %  post_detail.title
		return context
