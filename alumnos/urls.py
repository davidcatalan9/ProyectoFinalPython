from django.urls import path
from . import views


app_name = 'alumnos'
urlpatterns = [
    path( '', views.index, name='index' ),
    path( 'formulario', views.formulario, name='formulario'), 
    path( 'detalle/<int:alumnos_id>', views.detalleNew, name='listaAlum' )
        
]





