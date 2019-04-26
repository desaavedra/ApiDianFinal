from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ReporteForm
from .models import Reporte
from django.http import HttpResponse
import hmac
import hashlib
import base64
import requests


def registrar(request):
    #    hashLocal = hashlib.new("sha256", request)
    #   digestLocal = hashLocal.digest()
    form = ReporteForm(request.POST or None)
    if form.is_valid():
        digestRecibido = form.cleaned_data['hash']
        hashLocal = hashlib.new("sha256", form.cleaned_data['informacion'])
        digestLocal = hashLocal.digest()
        if digestRecibido == digestLocal:
            form.save()
            form = ReporteForm()
        else:
             return HttpResponse("El hash no es correcto")
    context = {
        'form': form,
    }
    return render(request, 'Post_reportes.html', context)


def index(request):
    return render(request, 'base.html', {})


def listarReportes(request):
    queryset = Reporte.objects.all()
    context = {
        'reporte_list': queryset
    }
    return render(request, 'List_Reportes.html', context)
