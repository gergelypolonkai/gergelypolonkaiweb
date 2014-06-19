from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post, CodeChunk

def mainpage(request):
    last_posts = Post.objects.filter(draft = False).order_by('-created_at')[:5]
    return render(request, 'blog/listing.html', {'posts': last_posts})

def listing(request, tag, year, month, day, page):
    kwargs = {}
    kwargs['draft'] = False

    view = index
    if (tag == None):
        view = "index"
    else:
        kwargs['tags__slug'] = tag
        view = "tag"

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

    return render(request, 'blog/listing.html', { 'posts': posts, 'view': "blog:" + view })

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
    post = get_object_or_404(Post, created_at__year=int(year), created_at__month=int(month), created_at__day=int(day), slug=slug, draft=False)
    return render(request, 'blog/view.html', {'post': post})

def codechunk(request, language, slug):
    chunk = get_object_or_404(CodeChunk, language=language, slug=slug)
    return render(request, 'blog/code-chunk.html', {'codechunk': chunk})

def feed(request):
    return render(request, 'blog/feed.xml', {})

