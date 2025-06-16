from django.contrib import admin
from .models import Alumno, Bachiller, Documentacion

admin.site.register(Alumno)
admin.site.register(Bachiller)
admin.site.register(Documentacion)