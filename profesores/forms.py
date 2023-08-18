from . import models
from django.forms import ModelForm

class ProfesorForm(ModelForm):
    class Meta:
        model = models.Profesor
        fields = ['nombre', 'apellido', 'profesion', 'email', 'fechaNacimiento', 'curso' ]
        