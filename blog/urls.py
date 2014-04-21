from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^$',                                                             views.index,     name = 'index'),
    url(r'^page/(?P<page>\d+)$',                                           views.indexpage, name = 'indexpage'),
    url(r'^tag/(?P<tag>[^/]+)$',                                           views.taglist,   name = 'taglist'),
    url(r'^tag/(?P<tag>[^/]+)/page/(?P<page>\d+)$',                        views.tagpage,   name = 'tagpage'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/?$',                  views.datelist,  name = 'datelist'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/page/(?P<page>\d+)$', views.datepage,  name = 'datepage'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[^/]+)$',    views.read,      name = 'read'),
    url(r'^code-chunk/(?P<language>[^/]+)/(?P<slug>[^/]+)$',               views.codechunk, name = 'codechunk'),
    url(r'^feed$',                                                         views.feed,      name = 'feed'),
)
