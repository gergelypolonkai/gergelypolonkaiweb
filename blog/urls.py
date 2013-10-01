from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^$',                                                          views.index,   name='index'),
    url(r'^feed$',                                                      views.feed,    name='feed'),
    url(r'^tag/(?P<tag>.*)$',                                           views.taglist, name='taglist'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[^/]+)$', views.read,    name='read'),
)
