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
    body = render_to_string('basics/notfound.html', {})
    return HttpResponse(body, status_code = 404)

def serverror(request):
    body = render_to_string('basics/serverror.html', {})
    return HttpResponse(body, status_code = 500)

def forbidden(request):
    body = render_to_string('basics/forbidden.html', {})
    return HttpResponse(body, status_code = 403)

def badrequest(request):
    body = render_to_string('basics/badrequest.html', {})
    return HttpResponse(body, status_code = 400)
