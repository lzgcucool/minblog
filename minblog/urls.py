"""minblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from .views import IndexView, AboutView, PostDetail


urlpatterns = [
   url(r'^$', IndexView.as_view(), name='index'),
   url(r'^tag_(?P<tag>\w+)/$', IndexView.as_view(), name='tags'),
   url(r'^arch_(?P<arch_year>\d+)-(?P<arch_month>\d+)/$', IndexView.as_view(), name='arch_date'),
   url(r'^about/', AboutView.as_view(), name='about'),
   url(r'^(?P<slug>\w+)/$', PostDetail.as_view(), name='post_detail'),
]
