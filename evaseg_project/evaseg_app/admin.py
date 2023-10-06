from django.contrib import admin

# Register your models here.

from evaseg_app.models import Rol, TipoDocumento, Usuario, Login, Ficha, InstructorFicha, AprendizFicha, TipoProceso, DetalleProceso, Citacion
admin.site.register([Rol, TipoDocumento, Usuario, Login, Ficha, InstructorFicha, AprendizFicha, TipoProceso, DetalleProceso, Citacion])