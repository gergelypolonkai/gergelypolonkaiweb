from django.shortcuts import render
from django.contrib.sites.models import get_current_site
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from StringIO import StringIO
from xhtml2pdf import pisa

def googlevalidator(request):
    return HttpResponse('')

def resumelink(request):
    return request.build_absolute_uri(reverse('basics:resumepdf'))

def resumepdf(request):
    body = render_to_string('basics/resume.html', {
            'resume_link': resumelink(request),
            'pdf': True
        })
    dst = StringIO()
    pdf = pisa.CreatePDF(body, dst)
    pdf_data = dst.getvalue()
    dst.close()

    if not pdf.err:
        return HttpResponse(pdf_data, content_type = 'application/pdf')

    return HttpResponse('We had some errors: <pre>%s</pre>' % escape(html))

def resume(request):
    return render(request, 'basics/resume.html', {
            'resume_link': resumelink(request)
        })

def about(request):
    return render(request, 'basics/about.html', {})

def disclaimer(request):
    return render(request, 'basics/disclaimer.html', {})

def notfound(request):
    return TemplateResponse(request, 'basics/notfound.html', status = 404).render()

def serverror(request):
    return TemplateResponse(request, 'basics/serverror.html', status = 500).render()

def forbidden(request):
    return TemplateResponse(request, 'basics/forbidden.html', status = 403).render()

def badrequest(request):
    return TemplateResponse(request, 'basics/badrequest.html', status = 400).render()
