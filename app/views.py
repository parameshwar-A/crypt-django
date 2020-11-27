from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage.html')

def instructions(request):
    return render(request, 'instructions.html')

def contact(request):
    return render(request, 'contact.html')

