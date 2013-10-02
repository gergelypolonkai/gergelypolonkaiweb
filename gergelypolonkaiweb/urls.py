from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',                      'blog.views.mainpage',          name='home'),
    url(r'^google150e54bda5f96d97', 'basics.views.googlevalidator'),
    url(r'^blog/',                  include('blog.urls',            namespace='blog')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/',             include('django.contrib.admindocs.urls')),
    url(r'^admin/',                 include(admin.site.urls)),
    url(r'^',                       include('basics.urls',          namespace='basics')),
)
