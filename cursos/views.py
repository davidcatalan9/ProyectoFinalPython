from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_list_or_404

import cursos

from profesores.models import Curso

# Create your views here.
def listaCursos(request):
    CursosData = Curso.objects.all()
    
    return render(
        request,
        'listaCursos.html',
        context={'cursos':CursosData}
    )

def detalleCurso(request, curso_id):
    cursoDet = Curso.objects.get(id=curso_id)
    print(cursoDet)
    return render(
        request, 'detalleCurso.html', 
        context={'curso':cursoDet}
        )