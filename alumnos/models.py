from django.db import models

from profesores.models import Curso, Trabajos

# Create your models here.
class Alumnos(models.Model):
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    direccion = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=30)
    curso = models.ForeignKey( Curso, on_delete=models.DO_NOTHING )
    trabajos = models.ForeignKey( Trabajos, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return ( self.nombre + " " +self.apellido )
    
    