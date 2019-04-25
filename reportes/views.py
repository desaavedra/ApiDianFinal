from django.shortcuts import render
from .forms import ReporteForm
from .models import Reporte
from django.http import HttpResponse
import hmac
import hashlib
import base64

def _hmac_is_valid(body, secret, hmac_to_verify):
    hash            = hmac.new(body, secret, hashlib.sha256)
    hmac_calculated = base64.b64encode(hash.digest())
    return hmac_calculated == hmac_to_verify

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
