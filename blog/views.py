from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post, CodeChunk
from django.core.urlresolvers import reverse
import datetime
import pytz
from django.templatetags.static import static

def mainpage(request):
    last_posts = Post.objects.filter(draft = False).order_by('-created_at')[:5]
    return render(request, 'blog/listing.html', {'posts': last_posts})

def listing(request, tag, year, month, day, page):
    kwargs = {}
    kwargs['draft'] = False

    view = 'index'

    if (tag == None):
        view = 'index'
    else:
        kwargs['tags__slug'] = tag
        view = 'tag'

    if (year != None):
        kwargs['created_at__year'] = year

        if (month != None):
            kwargs['created_at__month'] = month

            if (day != None):
                kwargs['created_at__day'] = day

    post_list = Post.objects.filter(**kwargs)
    paginator = Paginator(post_list.order_by('-created_at'), 10)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if paginator.num_pages > 1:
        view = view + 'page'

    return render(request, 'blog/listing.html', {
            'posts': posts,
            'tag': tag,
            'view': "blog:" + view
        })

def index(request):
    return listing(request, None, None, None, None, 1)

def indexpage(request, page):
    return listing(request, None, None, None, None, page)

def taglist(request, tag):
    return listing(request, tag, None, None, None, 1)

def tagpage(request, tag, page):
    return listing(request, tag, None, None, None, page)

def datelist(request, year, month, day):
    return listing(request, None, year, month, day, 1)

def datepage(request, year, month, day, page):
    return listing(request, None, year, month, day, page)

def read(request, year, month, day, slug):
    post = get_object_or_404(Post,
            created_at__year = int(year),
            created_at__month = int(month),
            created_at__day = int(day),
            slug = slug,
            draft = False
        )
    next_post = Post.objects.filter(created_at__gt = post.created_at).order_by('created_at')[0:1]
    prev_post = Post.objects.filter(created_at__lt = post.created_at).order_by('-created_at')[0:1]

    if not next_post:
        next_post = None
    else:
        next_post = next_post[0]

    if not prev_post:
        prev_post = None
    else:
        prev_post = prev_post[0]

    return render(request, 'blog/view.html', {
            'post': post,
            'prev_post': prev_post,
            'next_post': next_post,
        })

def codechunk(request, language, slug):
    chunk = get_object_or_404(CodeChunk, language = language, slug = slug)
    return render(request, 'blog/code-chunk.html', {'codechunk': chunk})

def feed(request):
    latest_post = Post.objects.filter(draft = False).order_by('-created_at')[0:1]

    if not latest_post:
        latest_date = datetime.datetime(1983, 3, 7, 11, 54, 45, 0, pytz.timezone('Europe/Budapest'))
    else:
        latest_date = latest_post[0].created_at

    posts = Post.objects.order_by('-created_at')[:10]

    return render(request, 'blog/feed.xml', {
                    'site_url': request.build_absolute_uri(reverse('home')),
                    'profile_pic': request.build_absolute_uri(static('images/profile.png')),
                    'last_build_date': latest_date.strftime('%a, %d %b %Y %T %z'),
                    'posts': posts,
                },
            content_type = 'application/xml'
        )

