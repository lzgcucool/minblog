from django.contrib import admin
from minblog.models import Post, PostTags
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    """docstring for PostAdmin"""
    list_display = ['title','pubtime']
    search_fields = ['title']
    list_filter = ['pubtime']
    filter_horizontal = ('posttags',)


admin.site.register(PostTags)
admin.site.register(Post, PostAdmin)