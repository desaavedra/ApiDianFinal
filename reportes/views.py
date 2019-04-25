from django.shortcuts import render
from .forms import ReporteForm
from .models import Reporte
from django.http import HttpResponse


def index(request):
    return render(request, 'base.html', {})


def registrar(request):


    form = ReporteForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ReporteForm()
    context = {
        'form': form,
    }
    return render(request, 'Post_reportes.html', context)

def listarReportes(request):
    queryset = Reporte.objects.all()
    context = {
        'reporte_list' : queryset
    }
    return render(request, 'List_Reportes.html', context)
