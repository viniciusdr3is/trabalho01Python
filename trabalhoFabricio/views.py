from django.shortcuts import render

def pagina_inicial_personalizada(request):
    return render(request, 'index.html')