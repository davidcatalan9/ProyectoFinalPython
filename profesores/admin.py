from django.contrib import admin
from .models import Profesor, Curso, Trabajos

class ProfesorAdmin( admin.ModelAdmin):    
    list_display = ('id', 'nombre', 'apellido','curso')
    
class CursoAdmin(admin.ModelAdmin):
    exclude = ('creacion',)
    list_display = ('id', 'nombre')
    
class TrabajosAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','descripcion')
    
# Register your models here.
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Trabajos, TrabajosAdmin)



