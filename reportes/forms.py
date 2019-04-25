from django import forms

from .models import Reporte

class ReporteForm(forms.ModelForm):
    hash = forms.CharField(max_length=200)
    json = forms.FileField()

    class Meta:
        model = Reporte
        fields = ['hash', 'json']
        labels = {
            'Hash': 'Hash',
            'Archivo Json': 'archivoJson',

        }
