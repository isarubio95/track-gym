from django.contrib import admin
from .models import Actividad, Ejercicio, TipoEjercicio

class EjercicioInline(admin.TabularInline):
    model = Ejercicio
    extra = 1

@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'fecha')
    list_filter = ('usuario', 'fecha')
    inlines = [EjercicioInline]

admin.site.register(TipoEjercicio)
admin.site.register(Ejercicio)