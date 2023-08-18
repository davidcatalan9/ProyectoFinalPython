from django.contrib import admin

# Register your models here.
from .models import Alumnos

class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'apellido' )

admin.site.register(Alumnos, AlumnoAdmin )

