from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ProfesorForm
from .models import Profesor

# Create your views here.
@login_required
def index(request):
    profesores = Profesor.objects.all()
    
    return render(
        request, 
        'baseProf.html', 
        context= {'profesores': profesores } 
    )

@login_required    
def detalleProf(request, profesor_id):
        profesor = get_object_or_404(Profesor, id=profesor_id)
    
        return render(
            request,
            'detalleProf.html', 
            context= { 'profesor': profesor } )


@login_required        
def modificaProf(request, profesor_id ):
        profesor = get_object_or_404( Profesor, id=profesor_id)
    
        if request.method == 'POST':
            form = ProfesorForm(request.POST, instance=profesor)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/profesores')
        else:
            form = ProfesorForm(instance=profesor)
        
        return render(
            request,
            'profesor_form.html',
            {'form':form} )
    
    
@login_required
def formulario(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/profesores')
    else:
        form = ProfesorForm()
    
    return render(
        request,
        'profesor_form.html',
        {'form': form} 
    )
    
    

@login_required
def eliminaProf(request, profesor_id):
    profesor = get_object_or_404(Profesor, id=profesor_id)
    
    if request.method == 'POST':
        profesor.delete()
        messages.success(request, f"El profesor {profesor} ha sido eliminado.")
        return HttpResponseRedirect('/profesores')
    
    return render(
        request,
        'elimina_profesor.html',
        {'profesor': profesor}
    )
