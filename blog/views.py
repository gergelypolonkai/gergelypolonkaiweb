import datetime
from django.shortcuts import render, get_object_or_404
from blog.models import Post

def index(request):
    last_posts = Post.objects.order_by('-created_at')[:5]
    context = { 'posts': last_posts }
    return render(request, 'blog/listing.html', context)

def read(request, year, month, day, slug):
    post = get_object_or_404(Post, created_at__year=int(year), created_at__month=int(month), created_at__day=int(day), slug=slug);
    return render(request, 'blog/view.html', {'post': post})

def feed(request):
    return render(request, 'blog/feed.xml', {})

def resume(request):
    return render(request, 'resume.html', {})

def about(request):
    return renden(request, 'about.html', {})

def disclaimer(request):
    return renden(request, 'disclaimer.html', {})
