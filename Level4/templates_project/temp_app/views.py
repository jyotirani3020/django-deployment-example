from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'temp_app/index.html')

def other(request):
    return render(request, 'temp_app/other.html')

def relative(request):
    return render(request, 'temp_app/relative_urls_templates.html')