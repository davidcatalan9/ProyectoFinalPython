from django import forms
from .models import Alumnos, Trabajos
from alumnos import models

class AlumnosForm(forms.ModelForm):
    # Trabajos = forms.ModelMultipleChoiceField(queryset=Trabajos.objects.all())
    class Meta:
        model = models.Alumnos
        fields = ['rut', 'nombre', 'apellido', 'direccion', 'ciudad', 'curso', 'trabajos' ]
        