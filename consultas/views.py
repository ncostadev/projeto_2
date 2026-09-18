from django.shortcuts import render, redirect, get_object_or_404
from .models import Consulta
from django import forms
# Create your views here.

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = '__all__'


def home_consultas(request):
    quantidade_consultas = Consulta.objects.count()
    consultas = Consulta.objects.all()
    
    return render(request, 'pages/home_consultas.html', {'quantidade_consultas': quantidade_consultas, 'consultas': consultas})


def cadastrar(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_consulta')
    else:
        form = ConsultaForm()
        
    return render(request, 'pages/cadastrar.html', {'form': form})


def editar(request, id):
    consulta = get_object_or_404(Consulta, id=id)

    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)

        if form.is_valid():
            form.save()
            return redirect('home_consulta')
    else:
        form = ConsultaForm(instance=consulta)

    return render(request, 'pages/editar.html', {'form': form, 'consulta': consulta})

def excluir(request, id):
    consulta = get_object_or_404(Consulta, id=id)

    if request.method == 'POST':
        consulta.delete()
        return redirect('home_consultas')

    return render(request, 'pages/home_consultas.html', {'consulta': consulta})

