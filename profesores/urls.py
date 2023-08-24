from django.urls import path
from . import views


app_name = 'profesor'
urlpatterns = [
    path( ''                 , views.index     , name='index' ),
    path( 'formulario'       , views.formulario, name="formulario"),
    path( 'detalleProf/<int:profesor_id>', views.detalleProf, name='detalleProf' ),
    path( 'modProf/<int:profesor_id>/' , views.modificaProf, name='modificaProf' ),
    path( 'profesores/<int:profesor_id>/eliminar/', views.eliminaProf, name='elimina_profesor'),
]
