from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.http import HttpResponse

admin.autodiscover()

handler404 = 'basics.views.notfound'
handler500 = 'basics.views.serverror'
handler403 = 'basics.views.forbidden'
handler400 = 'basics.views.badrequest'

urlpatterns = patterns('',
    url(
            r'^$',
            'blog.views.mainpage',
            name = 'home'
        ),
    url(
            r'^google150e54bda5f96d97',
            lambda r: HttpResponse("", mimetype="text/plain")
        ),
    url(
            r'^robots\.txt$',
            TemplateView.as_view(template_name = 'robots.txt', content_type = 'text/plain')
        ),
    url(
            r'^blog/',
            include(
                    'blog.urls',
                    namespace = 'blog'
                )
        ),
    # Uncomment the admin/doc line below to enable admin documentation:
    #url(
    #        r'^admin/doc/',
    #        include('django.contrib.admindocs.urls')
    #    ),
    url(
            r'^admin/',
            include(admin.site.urls)
        ),
    url(
            r'^',
            include(
                    'basics.urls',
                    namespace = 'basics'
                )
        ),
)
