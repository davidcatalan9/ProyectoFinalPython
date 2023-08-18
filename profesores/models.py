from django.db import models
from django.utils import timezone

# from alumnos.models import Alumnos


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    camada = models.IntegerField()
    creacion = models.DateTimeField(default=timezone.now) 
    
    def __str__(self):
        return self.nombre
    
    
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    profesion = models.CharField(max_length=50)
    email = models.EmailField()
    fechaNacimiento = models.DateField()
    curso = models.ForeignKey( Curso, on_delete=models.DO_NOTHING )
    
    def __str__(self):
        return ( self.nombre +" " + self.apellido )
    
    
class Trabajos(models.Model):
    nombre = models.CharField(max_length=15)
    descripcion = models.CharField(max_length=100)
    fechaVence = models.DateField()
    nota = models.IntegerField()
    curso = models.ForeignKey( Curso, on_delete=models.DO_NOTHING )

    def __str__(self):
        return ('Trabajo: ' + self.nombre)
