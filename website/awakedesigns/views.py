from django.shortcuts import render

def index(request):
    return render(request, 'awakedesigns/home.html')

def contact(request):
    return render(request, 'awakedesigns/basic.html')

def services(request):
    return render(request, 'awakedesigns/services.html')

def about(request):
    return render(request, 'awakedesigns/about.html')

def portfolio(request):
    return render(request, 'awakedesigns/portfolio.html')

def downloads(request):
    return render(request, 'awakedesigns/downloads.html')
