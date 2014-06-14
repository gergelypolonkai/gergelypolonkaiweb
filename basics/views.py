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

def notfound(request):
    return render(request, 'basics/notfound.html', {})

def serverror(request):
    return render(request, 'basics/serverror.html', {})

def forbidden(request):
    return render(request, 'basics/forbidden.html', {})

def badrequest(request):
    return render(request, 'basics/badrequest.html', {})
