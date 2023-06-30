from django.shortcuts import render

def home(request):
    from pages.nametest import name
    return render(request, 'home.html', {'name_func': name})

def about(request):
    return render(request, 'about.html', {})