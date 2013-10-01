from django.conf.urls import patterns, url
from basics import views

urlpatterns = patterns('',
    url(r'^resume',     views.resume,     name='resume'),
    url(r'^about',      views.about,      name='about'),
    url(r'^disclaimer', views.disclaimer, name='disclaimer'),
)
