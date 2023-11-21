from django.contrib import admin

# Register your models here.
from Apps.App_Admin.models import Admin
from Apps.App_Usuario.models import Usuario
from Apps.App_Principal.models import Permisos, Ciiu_nivel2, Ciiu_Operacinal, Entidad_Bancaria, Persona

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Admin)
admin.site.register(Ciiu_nivel2)
admin.site.register(Ciiu_Operacinal)
admin.site.register(Entidad_Bancaria)
admin.site.register(Persona)

class TablaPermiso(admin.ModelAdmin):
    list_display = ['id_usuario','fecha_inicio','fecha_fin','con_directivo','personas','data_principal','accionistas','junta','cargos','origen','impuesto_causado','entidades','auditores','apalancamiento','ciu','estado_permiso']
    search_fields = ['id_usuario']
    list_per_page = 5

admin.site.register(Permisos,TablaPermiso)