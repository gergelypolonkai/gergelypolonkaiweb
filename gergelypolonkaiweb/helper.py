from django.db.models import Count
from taggit.models import Tag
from math import floor
from operator import itemgetter
from django.conf import settings
import os
from random import choice

def randomheader(request):
    header_file = choice(filter(lambda x: os.path.isfile(settings.HEADER_DIR + os.path.sep + x), os.listdir(settings.HEADER_DIR)))
    return {'header': header_file}

def tagcloud(request):
    tagcloudlist = Tag.objects.annotate(ct=Count('taggit_taggeditem_items')).order_by('-ct')

    if (len(tagcloudlist) > 0):
        tmax = tagcloudlist[0].ct
        tmin = 1

    if (tmax == tmin):
        tmax += 1

    tagcloud = []

    for cloudelement in tagcloudlist:
        tagcount = cloudelement.ct

        if (tagcount >= tmin):
            size = int(floor((5.0 * (tagcount - tmin)) / (tmax - tmin)))
            tagcloud.append({'name': cloudelement.name, 'slug': cloudelement.slug, 'size': size})

    tagcloud.sort(key=itemgetter('name'))

    return {'tagcloud': tagcloud}

def viewname(request):
    return {
        'view_name': request.view_name,
    }
