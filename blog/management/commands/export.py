# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError

import codecs
import textwrap
import html2text

from blog.models import Post

class Command(BaseCommand):
    help = 'Export all posts to HTML files'

    def handle(self, *args, **options):
        for post in Post.objects.all():
            # TODO: Change this to a sane path!
            filename = '/home/polesz/posts/%d-%02d-%02d-%s.markdown' % (post.created_at.year, post.created_at.month, post.created_at.day, post.slug)

            with codecs.open(filename, 'w', 'utf-8') as f:
                f.write('---\n')
                f.write('layout:    default\n')
                f.write('title:     "%s"\n' % post.title)
                # date:   2011-06-10 14:20:43
                f.write('date:      %s\n' % post.created_at)
                if post.tags.all().count() > 0:
                    f.write('tags:     ')

                    for tag in post.tags.all():
                        f.write(' %s' % tag.__unicode__().lower())

                    f.write('\n')
                f.write('permalink: /blog/%d/%d/%d/%s\n' % (post.created_at.year, post.created_at.month, post.created_at.day, post.slug))
                f.write('published: true\n')
                f.write('author:    %s %s <%s>\n' % (post.user.first_name, post.user.last_name, post.user.email))
                f.write('---\n\n')

                h = html2text.HTML2Text()
                try:
                    f.write(h.handle(post.content))
                except Exception:
                    print post.content
                    raise

            self.stdout.write(filename)
