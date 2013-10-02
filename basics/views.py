from django.shortcuts import render
from django.contrib.sites.models import get_current_site
from django.http import HttpResponse

def googlevalidator(request):
    return HttpResponse('')

def resume(request):
    return render(request, 'basics/resume.html', { 'site': get_current_site(request) })

def about(request):
    return render(request, 'basics/about.html', {})

def disclaimer(request):
    return render(request, 'basics/disclaimer.html', {})
