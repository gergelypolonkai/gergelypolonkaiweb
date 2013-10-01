from django.shortcuts import render

def resume(request):
    return render(request, 'resume.html', {})

def about(request):
    return render(request, 'basics/about.html', {})

def disclaimer(request):
    return render(request, 'basics/disclaimer.html', {})
