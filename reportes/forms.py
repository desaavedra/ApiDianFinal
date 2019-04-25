from django import forms

from .models import Reporte

class ReporteForm(forms.ModelForm):
    hash = forms.CharField(max_length=200)
    informacion = forms.CharField(max_length=1048575)

    class Meta:
        model = Reporte
        fields = ['hash', 'informacion']
        labels = {
            'Hash': 'Hash',
            'Informacion': 'informacion',

        }
