from django.db.models import Count
from taggit.models import Tag
from math import floor

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

    tagcloud.sort(key=lambda k: k['name'])

    return {'tagcloud': tagcloud}
