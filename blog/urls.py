from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^$',                                                          views.index,   name='index'),
    url(r'^feed$',                                                      views.feed,    name='feed'),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/(?P<slug>[^/]+)$', views.read,    name='read'),
    url(r'^resume',                                                     views.resume,  name='resume'),
    url(r'^about',                                                      views.resume,  name='about'),
    url(r'^disclaimer',                                                 views.resume,  name='disclaimer'),
)
