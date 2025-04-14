from django.shortcuts import render

def home(request):
    return render(request, 'apresentacao/home.html')

def sobre(request):
    return render(request, 'apresentacao/sobre.html')

def contato(request):
    return render(request, 'apresentacao/contato.html')