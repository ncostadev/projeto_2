from django.shortcuts import render

# Create your views here.

def home_consultas(request):
    return render(request, 'pages/consultar.html')


def cadastrar(request):
    return render(request, 'pages/cadastrar.html')


def editar(request):
    return render(request, 'pages/editar.html')
