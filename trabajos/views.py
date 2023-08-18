from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
import trabajos

from profesores.models import Trabajos



@login_required
def listaTrabajos(request):
    TrabajosLis = Trabajos.objects.all()
    
    return render(
        request, 
        'listaTrabajos.html',
        context={'trabajos':TrabajosLis}
    )

