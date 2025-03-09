from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'personalsite/base.html')

def contact(request):
    return render(request, 'personalsite/contact.html')

def education(request):
    return render(request, 'personalsite/education.html')

def resume(request):
    return render(request, 'personalsite/resume.html')