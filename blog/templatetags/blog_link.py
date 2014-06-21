from django import template
from django.core.urlresolvers import reverse

register = template.Library()

@register.simple_tag(takes_context = True)
def get_post_link(context, post):
    return context['request'].build_absolute_uri(reverse('blog:read', args=(post.created_at.year, post.created_at.month, post.created_at.day, post.slug)))
