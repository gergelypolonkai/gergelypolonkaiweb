from django import template
from django.core.urlresolvers import reverse
from django.conf import settings
import pytz

register = template.Library()

@register.simple_tag
def get_post_relative_link(post):
    post_date = post.created_at.astimezone(pytz.timezone(settings.TIME_ZONE))
    return reverse('blog:read', args=(post_date.year, post_date.month, post_date.day, post.slug))

@register.simple_tag(takes_context = True)
def get_post_link(context, post):
    return context['request'].build_absolute_uri(get_post_relative_link(post))

