from django.shortcuts import render, redirect
from .models import Consulta
from django import forms
# Create your views here.

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'


def home_consultas(request):
    return render(request, 'pages/consultar.html')


def cadastrar(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_consultas')
    else:
        form = ConsultaForm()
    return render(request, 'pages/cadastrar.html', {'form': form})


def editar(request):
    return render(request, 'pages/editar.html')
