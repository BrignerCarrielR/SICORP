from django.contrib import admin
from django.urls import path

from Apps.App_Admin.views import InicioTemplateView, InicioCiiu, Lista_Ciiu_Nivel2, Nuevo_Ciiu_Nivel2, \
    Modificar_Ciiu_Nivel2, Eliminar_Ciiu_Nivel2, Nuevo_Ciiu_Operacinal, Lista_Ciiu_Operacinal, \
    Modificar_Ciiu_Operacinal, Eliminar_Ciiu_Operacinal, Lista_Cargo, Nuevo_Cargo, Modificar_Cargo, Eliminar_Cargo, \
    Inicio_Orignes, Lista_Pais, Nuevo_Pais, Modificar_Pais, Eliminar_Pais, Lista_Provincia, Eliminar_Provincia, \
    Modificar_Provincia, Nuevo_Provincia, Lista_Ciudad, Nuevo_Ciudad, Modificar_Ciudad, Eliminar_Ciudad, \
    Eliminar_Entidad, Modificar_Entidad, Nuevo_Entidad, Lista_Entidad, Lista_Persona, Nuevo_Persona, Modificar_Persona, \
    Eliminar_Persona, Lista_Apalancamiento, Nuevo_Apalancamiento, Modificar_Apalancamiento, Eliminar_Apalancamiento, \
    Lista_Accionista, Eliminar_Accionista, Modificar_Accionista, Nuevo_Accionista, Lista_Junta, Nuevo_Junta, \
    Modificar_Junta, Eliminar_Junta, Eliminar_Consejo_directivo, Lista_Consejo_directivo, Nuevo_Consejo_directivo, \
    Modificar_Consejo_directivo, Auditores, Lista_Auditor_interno, Nuevo_Auditor_interno, Modificar_Auditor_interno, \
    Eliminar_Auditor_interno, Modificar_Auditor_externo, Eliminar_Auditor_externo, Nuevo_Auditor_externo, \
    Lista_Auditor_externo, Excel, Data_principal, Recuperar_contrauser

from Apps.App_Admin.views import Lista_Permiso, Modulos_Admin, Nuevo_Permiso, login_Admin, CerrarSecionAdmin, \
    Modificar_Permiso, Eliminar_Permiso
from Apps.App_Usuario.views import user_Modulos_Usuario, login_Usuario, CerrarSecionUser, user_Registrar_Usuario, \
    user_Recuperar_contrauser, user_InicioCiiu, user_Lista_Ciiu_Nivel2, user_Nuevo_Ciiu_Nivel2, \
    user_Modificar_Ciiu_Nivel2, user_Eliminar_Ciiu_Nivel2, user_Nuevo_Ciiu_Operacinal, user_Lista_Ciiu_Operacinal, \
    user_Modificar_Ciiu_Operacinal, user_Eliminar_Ciiu_Operacinal, user_Lista_Cargo, user_Nuevo_Cargo, \
    user_Modificar_Cargo, user_Eliminar_Cargo, \
    user_Inicio_Orignes, user_Lista_Pais, user_Nuevo_Pais, user_Modificar_Pais, user_Eliminar_Pais, \
    user_Lista_Provincia, user_Eliminar_Provincia, \
    user_Modificar_Provincia, user_Nuevo_Provincia, user_Lista_Ciudad, user_Nuevo_Ciudad, user_Modificar_Ciudad, \
    user_Eliminar_Ciudad, \
    user_Eliminar_Entidad, user_Modificar_Entidad, user_Nuevo_Entidad, user_Lista_Entidad, user_Lista_Persona, \
    user_Nuevo_Persona, user_Modificar_Persona, \
    user_Eliminar_Persona, user_Lista_Apalancamiento, user_Nuevo_Apalancamiento, user_Modificar_Apalancamiento, \
    user_Eliminar_Apalancamiento, \
    user_Lista_Accionista, user_Eliminar_Accionista, user_Modificar_Accionista, user_Nuevo_Accionista, user_Lista_Junta, \
    user_Nuevo_Junta, \
    user_Modificar_Junta, user_Eliminar_Junta, user_Eliminar_Consejo_directivo, user_Lista_Consejo_directivo, \
    user_Nuevo_Consejo_directivo, \
    user_Modificar_Consejo_directivo, user_Auditores, user_Lista_Auditor_interno, user_Nuevo_Auditor_interno, \
    user_Modificar_Auditor_interno, \
    user_Eliminar_Auditor_interno, user_Modificar_Auditor_externo, user_Eliminar_Auditor_externo, \
    user_Nuevo_Auditor_externo, \
    user_Lista_Auditor_externo, user_Excel, user_Data_principal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioTemplateView.as_view(), name="inicio"),
    path('admin_modulos', Modulos_Admin.as_view(), name="admin_modulos"),
    path('usuario_modulos', user_Modulos_Usuario.as_view(), name="usuario_modulos"),

    # login del usuario
    path('login_usuario', login_Usuario, name='login_usuario'),
    path('cerrarsecion_user', CerrarSecionUser, name='cerrarsecion_user'),
    path('registrar_usuario', user_Registrar_Usuario.as_view(), name='registrar_usuario'),
    path('recuperar_contraadmin', Recuperar_contrauser.as_view(), name='recuperar_contraadmin'),
    path('recuperar_contrauser', user_Recuperar_contrauser.as_view(), name='recuperar_contrauser'),


    # Loguin del admim
    path('login_admin', login_Admin, name='login_admin'),
    path('cerrarsecion_admin', CerrarSecionAdmin, name='cerrarsecion_admin'),

    path('lista_permiso', Lista_Permiso.as_view(), name="lista_permiso"),
    path('nuevo_permiso', Nuevo_Permiso.as_view(), name="nuevo_permiso"),
    path('modificar_permiso/<int:pk>', Modificar_Permiso.as_view(), name="modificar_permiso"),
    path('eliminar_permiso/<int:pk>', Eliminar_Permiso.as_view(), name="eliminar_permiso"),


    path('inicio_ciiu', InicioCiiu.as_view(), name="inicio_ciiu"),
    path('lista_ciiu_nivel2', Lista_Ciiu_Nivel2.as_view(), name="lista_ciiu_nivel2"),
    path('nuevo_ciiu_nivel2', Nuevo_Ciiu_Nivel2.as_view(), name="nuevo_ciiu_nivel2"),
    path('modificar_ciiu_nivel2/<int:pk>', Modificar_Ciiu_Nivel2.as_view(), name="modificar_ciiu_nivel2"),
    path('eliminar_ciiu_nivel2/<int:pk>', Eliminar_Ciiu_Nivel2.as_view(), name="eliminar_ciiu_nivel2"),


    path('lista_ciiu_operacinal', Lista_Ciiu_Operacinal.as_view(), name="lista_ciiu_operacinal"),
    path('nuevo_ciiu_operacinal', Nuevo_Ciiu_Operacinal.as_view(), name="nuevo_ciiu_operacinal"),
    path('modificar_ciiu_operacinal/<int:pk>', Modificar_Ciiu_Operacinal.as_view(), name="modificar_ciiu_operacinal"),
    path('eliminar_ciiu_operacinal/<int:pk>', Eliminar_Ciiu_Operacinal.as_view(), name="eliminar_ciiu_operacinal"),

    path('lista_cargo', Lista_Cargo.as_view(), name="lista_cargo"),
    path('nuevo_cargo', Nuevo_Cargo.as_view(), name="nuevo_cargo"),
    path('modificar_cargo/<int:pk>', Modificar_Cargo.as_view(), name="modificar_cargo"),
    path('eliminar_cargo/<int:pk>', Eliminar_Cargo.as_view(), name="eliminar_cargo"),

    path('inicio_origen', Inicio_Orignes.as_view(), name="inicio_origen"),

    path('lista_pais', Lista_Pais.as_view(), name="lista_pais"),
    path('nuevo_pais', Nuevo_Pais.as_view(), name="nuevo_pais"),
    path('modificar_pais/<int:pk>', Modificar_Pais.as_view(), name="modificar_pais"),
    path('eliminar_pais/<int:pk>', Eliminar_Pais.as_view(), name="eliminar_pais"),

    path('lista_provincia', Lista_Provincia.as_view(), name="lista_provincia"),
    path('nueva_provincia', Nuevo_Provincia.as_view(), name="nueva_provincia"),
    path('modificar_provincia/<int:pk>', Modificar_Provincia.as_view(), name="modificar_provincia"),
    path('eliminar_provincia/<int:pk>', Eliminar_Provincia.as_view(), name="eliminar_provincia"),

    path('lista_ciudad', Lista_Ciudad.as_view(), name="lista_ciudad"),
    path('nueva_ciudad', Nuevo_Ciudad.as_view(), name="nueva_ciudad"),
    path('modificar_ciudad/<int:pk>', Modificar_Ciudad.as_view(), name="modificar_ciudad"),
    path('eliminar_ciudad/<int:pk>', Eliminar_Ciudad.as_view(), name="eliminar_ciudad"),

    path('lista_entidad', Lista_Entidad.as_view(), name="lista_entidad"),
    path('nueva_entidad', Nuevo_Entidad.as_view(), name="nueva_entidad"),
    path('modificar_entidad/<int:pk>', Modificar_Entidad.as_view(), name="modificar_entidad"),
    path('eliminar_entidad/<int:pk>', Eliminar_Entidad.as_view(), name="eliminar_entidad"),

    path('lista_persona', Lista_Persona.as_view(), name="lista_persona"),
    path('nueva_persona', Nuevo_Persona.as_view(), name="nueva_persona"),
    path('modificar_persona/<int:pk>', Modificar_Persona.as_view(), name="modificar_persona"),
    path('eliminar_persona/<int:pk>', Eliminar_Persona.as_view(), name="eliminar_persona"),

    path('lista_apalancamiento', Lista_Apalancamiento.as_view(), name="lista_apalancamiento"),
    path('nueva_apalancamiento', Nuevo_Apalancamiento.as_view(), name="nueva_apalancamiento"),
    path('modificar_apalancamiento/<int:pk>', Modificar_Apalancamiento.as_view(), name="modificar_apalancamiento"),
    path('eliminar_apalancamiento/<int:pk>', Eliminar_Apalancamiento.as_view(), name="eliminar_apalancamiento"),

    path('lista_accionista', Lista_Accionista.as_view(), name="lista_accionista"),
    path('nuevo_accionista', Nuevo_Accionista.as_view(), name="nuevo_accionista"),
    path('modificar_accionista/<int:pk>', Modificar_Accionista.as_view(), name="modificar_accionista"),
    path('eliminar_accionista/<int:pk>', Eliminar_Accionista.as_view(), name="eliminar_accionista"),

    path('lista_junta', Lista_Junta.as_view(), name="lista_junta"),
    path('nuevo_junta', Nuevo_Junta.as_view(), name="nuevo_junta"),
    path('modificar_junta/<int:pk>', Modificar_Junta.as_view(), name="modificar_junta"),
    path('eliminar_junta/<int:pk>', Eliminar_Junta.as_view(), name="eliminar_junta"),


    path('lista_consejo_directivo', Lista_Consejo_directivo.as_view(), name="lista_consejo_directivo"),
    path('nuevo_consejo_directivo', Nuevo_Consejo_directivo.as_view(), name="nuevo_consejo_directivo"),
    path('modificar_consejo_directivo/<int:pk>', Modificar_Consejo_directivo.as_view(),
         name="modificar_consejo_directivo"),
    path('eliminar_consejo_directivo/<int:pk>', Eliminar_Consejo_directivo.as_view(),
         name="eliminar_consejo_directivo"),

    path('auditores', Auditores.as_view(), name="auditores"),

    path('lista_auditor_interno', Lista_Auditor_interno.as_view(), name="lista_auditor_interno"),
    path('nuevo_auditor_interno', Nuevo_Auditor_interno.as_view(), name="nuevo_auditor_interno"),
    path('modificar_auditor_interno/<int:pk>', Modificar_Auditor_interno.as_view(), name="modificar_auditor_interno"),
    path('eliminar_auditor_interno/<int:pk>', Eliminar_Auditor_interno.as_view(), name="eliminar_auditor_interno"),

    path('lista_auditor_externo', Lista_Auditor_externo.as_view(), name="lista_auditor_externo"),
    path('nuevo_auditor_externo', Nuevo_Auditor_externo.as_view(), name="nuevo_auditor_externo"),
    path('modificar_auditor_externo/<int:pk>', Modificar_Auditor_externo.as_view(), name="modificar_auditor_externo"),
    path('eliminar_auditor_externo/<int:pk>', Eliminar_Auditor_externo.as_view(), name="eliminar_auditor_externo"),


    path('subir_excel', Excel.as_view(), name="subir_excel"),
    path('data_principal', Data_principal.as_view(), name="data_principal"),

    #_______________________________________________________________________________________________________________

    path('user_inicio_ciiu', user_InicioCiiu.as_view(), name="user_inicio_ciiu"),
    path('user_lista_ciiu_nivel2', user_Lista_Ciiu_Nivel2.as_view(), name="user_lista_ciiu_nivel2"),
    path('user_nuevo_ciiu_nivel2', user_Nuevo_Ciiu_Nivel2.as_view(), name="user_nuevo_ciiu_nivel2"),
    path('user_modificar_ciiu_nivel2/<int:pk>', user_Modificar_Ciiu_Nivel2.as_view(), name="user_modificar_ciiu_nivel2"),
    path('user_eliminar_ciiu_nivel2/<int:pk>', user_Eliminar_Ciiu_Nivel2.as_view(), name="user_eliminar_ciiu_nivel2"),


    path('user_lista_ciiu_operacinal', user_Lista_Ciiu_Operacinal.as_view(), name="user_lista_ciiu_operacinal"),
    path('user_nuevo_ciiu_operacinal', user_Nuevo_Ciiu_Operacinal.as_view(), name="user_nuevo_ciiu_operacinal"),
    path('user_modificar_ciiu_operacinal/<int:pk>', user_Modificar_Ciiu_Operacinal.as_view(), name="user_modificar_ciiu_operacinal"),
    path('user_eliminar_ciiu_operacinal/<int:pk>', user_Eliminar_Ciiu_Operacinal.as_view(), name="user_eliminar_ciiu_operacinal"),

    path('user_lista_cargo', user_Lista_Cargo.as_view(), name="user_lista_cargo"),
    path('user_nuevo_cargo', user_Nuevo_Cargo.as_view(), name="user_nuevo_cargo"),
    path('user_modificar_cargo/<int:pk>', user_Modificar_Cargo.as_view(), name="user_modificar_cargo"),
    path('user_eliminar_cargo/<int:pk>', user_Eliminar_Cargo.as_view(), name="user_eliminar_cargo"),

    path('user_inicio_origen', user_Inicio_Orignes.as_view(), name="user_inicio_origen"),

    path('user_lista_pais', user_Lista_Pais.as_view(), name="user_lista_pais"),
    path('user_nuevo_pais', user_Nuevo_Pais.as_view(), name="user_nuevo_pais"),
    path('user_modificar_pais/<int:pk>', user_Modificar_Pais.as_view(), name="user_modificar_pais"),
    path('user_eliminar_pais/<int:pk>', user_Eliminar_Pais.as_view(), name="user_eliminar_pais"),

    path('user_lista_provincia', user_Lista_Provincia.as_view(), name="user_lista_provincia"),
    path('user_nueva_provincia', user_Nuevo_Provincia.as_view(), name="user_nueva_provincia"),
    path('user_modificar_provincia/<int:pk>', user_Modificar_Provincia.as_view(), name="user_modificar_provincia"),
    path('user_eliminar_provincia/<int:pk>', user_Eliminar_Provincia.as_view(), name="user_eliminar_provincia"),

    path('user_lista_ciudad', user_Lista_Ciudad.as_view(), name="user_lista_ciudad"),
    path('user_nueva_ciudad', user_Nuevo_Ciudad.as_view(), name="user_nueva_ciudad"),
    path('user_modificar_ciudad/<int:pk>', user_Modificar_Ciudad.as_view(), name="user_modificar_ciudad"),
    path('user_eliminar_ciudad/<int:pk>', user_Eliminar_Ciudad.as_view(), name="user_eliminar_ciudad"),

    path('user_lista_entidad', user_Lista_Entidad.as_view(), name="user_lista_entidad"),
    path('user_nueva_entidad', user_Nuevo_Entidad.as_view(), name="user_nueva_entidad"),
    path('user_modificar_entidad/<int:pk>', user_Modificar_Entidad.as_view(), name="user_modificar_entidad"),
    path('user_eliminar_entidad/<int:pk>', user_Eliminar_Entidad.as_view(), name="user_eliminar_entidad"),

    path('user_lista_persona', user_Lista_Persona.as_view(), name="user_lista_persona"),
    path('user_modificar_persona/<int:pk>', user_Modificar_Persona.as_view(), name="user_modificar_persona"),
    path('user_eliminar_persona/<int:pk>', user_Eliminar_Persona.as_view(), name="user_eliminar_persona"),

    path('user_lista_apalancamiento', user_Lista_Apalancamiento.as_view(), name="user_lista_apalancamiento"),
    path('user_nueva_apalancamiento', user_Nuevo_Apalancamiento.as_view(), name="user_nueva_apalancamiento"),
    path('user_modificar_apalancamiento/<int:pk>', user_Modificar_Apalancamiento.as_view(), name="user_modificar_apalancamiento"),
    path('user_eliminar_apalancamiento/<int:pk>', user_Eliminar_Apalancamiento.as_view(), name="user_eliminar_apalancamiento"),

    path('user_lista_accionista', user_Lista_Accionista.as_view(), name="user_lista_accionista"),
    path('user_nuevo_accionista', user_Nuevo_Accionista.as_view(), name="user_nuevo_accionista"),
    path('user_modificar_accionista/<int:pk>', user_Modificar_Accionista.as_view(), name="user_modificar_accionista"),
    path('user_eliminar_accionista/<int:pk>', user_Eliminar_Accionista.as_view(), name="user_eliminar_accionista"),

    path('user_lista_junta', user_Lista_Junta.as_view(), name="user_lista_junta"),
    path('user_nuevo_junta', user_Nuevo_Junta.as_view(), name="user_nuevo_junta"),
    path('user_modificar_junta/<int:pk>', user_Modificar_Junta.as_view(), name="user_modificar_junta"),
    path('user_eliminar_junta/<int:pk>', user_Eliminar_Junta.as_view(), name="user_eliminar_junta"),

    path('user_lista_consejo_directivo', user_Lista_Consejo_directivo.as_view(), name="user_lista_consejo_directivo"),
    path('user_nuevo_consejo_directivo', user_Nuevo_Consejo_directivo.as_view(), name="user_nuevo_consejo_directivo"),
    path('user_modificar_consejo_directivo/<int:pk>', user_Modificar_Consejo_directivo.as_view(),
         name="user_modificar_consejo_directivo"),
    path('eliminar_consejo_directivo/<int:pk>', user_Eliminar_Consejo_directivo.as_view(),
         name="user_eliminar_consejo_directivo"),

    path('user_auditores', user_Auditores.as_view(), name="user_auditores"),

    path('user_lista_auditor_interno', user_Lista_Auditor_interno.as_view(), name="user_lista_auditor_interno"),
    path('user_nuevo_auditor_interno', user_Nuevo_Auditor_interno.as_view(), name="user_nuevo_auditor_interno"),
    path('user_modificar_auditor_interno/<int:pk>', user_Modificar_Auditor_interno.as_view(), name="user_modificar_auditor_interno"),
    path('user_eliminar_auditor_interno/<int:pk>', user_Eliminar_Auditor_interno.as_view(), name="user_eliminar_auditor_interno"),

    path('user_lista_auditor_externo', user_Lista_Auditor_externo.as_view(), name="user_lista_auditor_externo"),
    path('user_nuevo_auditor_externo', user_Nuevo_Auditor_externo.as_view(), name="user_nuevo_auditor_externo"),
    path('user_modificar_auditor_externo/<int:pk>', user_Modificar_Auditor_externo.as_view(), name="user_modificar_auditor_externo"),
    path('user_eliminar_auditor_externo/<int:pk>', user_Eliminar_Auditor_externo.as_view(), name="user_eliminar_auditor_externo"),


    path('user_subir_excel', user_Excel.as_view(), name="user_subir_excel"),
    path('user_data_principal', user_Data_principal.as_view(), name="user_data_principal"),
]
