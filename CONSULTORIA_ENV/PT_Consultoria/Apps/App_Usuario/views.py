from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView, ListView
from datetime import datetime,timezone

from Apps.App_Usuario.forms import UsuarioForm
from Apps.App_Usuario.models import Usuario

from Apps.App_Principal.forms import Ciiu_nivel2Form, Ciiu_OperacinalForm, CargoForm, PaisForm,  ProvinciaForm, \
    CuidadForm, EntidadForm, PersonaForm, ApalancamientoForm, AccionistaForm, JuntaForm, Consejo_directivoForm, \
    Auditor_internoForm, Auditor_externoForm
from Apps.App_Principal.models import Permisos, Ciiu_nivel2, Ciiu_Operacinal, Cargo, Pais, Provincia, Cuidad, Entidad_Bancaria, \
    Persona, Apalancamiento, Accionista, Junta, Consejo_directivo, Auditor_interno, Auditor_externo

def login_Usuario(request):
    if request.method == 'POST':
        try:
            detalleUsuario = Usuario.objects.get(nom_user=request.POST['nom_user'],
                                                 contraseña=request.POST['contraseña'])
            request.session['ids'] = detalleUsuario.id
            request.session['nom_user'] = detalleUsuario.nom_user
            request.session['nombres'] = detalleUsuario.nombres
            request.session['correo'] = detalleUsuario.correo
            print(detalleUsuario.id)
            print(detalleUsuario.correo)

            return redirect('usuario_modulos')
        except Usuario.DoesNotExist as e:
            messages.success(request, 'Nombre de Usuario o Contraseña incorrecta..!')

    return render(request, 'usuario/login.html')

def CerrarSecionUser(request):
    try:
        del request.session['nom_user']
    except:
        return render(request, 'inicio.html')
    return render(request, 'inicio.html')

class user_Registrar_Usuario(CreateView):
    template_name = 'usuario/registrar_usuario.html'
    model = Usuario
    success_url = reverse_lazy('login_usuario')
    form_class = UsuarioForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Registrar'
        context['action_save'] = '/registrar_usuario'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_admin'
        context['volver'] = 'user_lista_permiso'
        context['action'] = 'add'
        return context

class user_Recuperar_contrauser(TemplateView):
    template_name = "usuario/recuperar_contraseña.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            usuarios = Usuario.objects.all()
            usuarios_list = list(usuarios.values())  # Convierte el QuerySet a lista de diccionarios
            context['usuarios_json'] = usuarios_list
            return context


class user_Modulos_Usuario(TemplateView):
    template_name = "usuario/modulos.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            permisos = Permisos.objects.all()
            fecha_actual = datetime.now()
            print(type(fecha_actual))
            print(fecha_actual)
            for per in permisos:
                if isinstance(per.fecha_fin, datetime):
                    # Convierte a offset-naive si es offset-aware
                    fecha_fin_naive = per.fecha_fin.astimezone(timezone.utc).replace(tzinfo=None)

                    if fecha_fin_naive > fecha_actual:
                        per.estado_permiso = 'En Curso'
                    else:
                        per.estado_permiso = 'Finalizado'
                    per.save()
                    print(per, per.estado_permiso)
            context['rol'] = 'USUARIO'
            context['voler_login'] = 'login_usuario'
            context['permisos'] = permisos
            return context

class user_InicioCiiu(TemplateView):
    template_name = "usuario/ciiu/modulos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Ciiu'
        context['rol'] = 'usuario'
        context['volver'] = 'usuario_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

# VISTAS DEL MODULO CIIU NIVEL2
class user_Lista_Ciiu_Nivel2(ListView):
    template_name = 'usuario/ciiu/ciiu_nivel2/lista_ciiu_nivel2.html'
    context_object_name = 'ciiu_nivel2'
    model = Ciiu_nivel2

    def get_queryset(self):
        queryset = super().get_queryset()
        nombres = self.request.GET.get('nombres')
        descripcion = self.request.GET.get('descripcion')
        if nombres:
            queryset = queryset.filter(ciiu__contains=nombres)
        if descripcion:
            queryset = queryset.filter(descripcion__contains=descripcion)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Ciiu Nivel 2'
        context['rol'] = 'usuario'
        context['nuevo'] = 'user_nuevo_ciiu_nivel2'
        context['volver'] = 'user_inicio_ciiu'
        context['query'] = self.request.GET.get("query") or ""
        return context

class user_Nuevo_Ciiu_Nivel2(CreateView):
    template_name = 'usuario/ciiu/ciiu_nivel2/nuevo_ciiu_nivel2.html'
    model = Ciiu_nivel2
    success_url = reverse_lazy('user_lista_ciiu_nivel2')
    form_class = Ciiu_nivel2Form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Ciiu Nivel 2'
        context['crud'] = ' Agregar'
        context['action_save'] = 'user_nuevo_ciiu_nivel2'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_ciiu_nivel2'
        context['action'] = 'add'
        return context

class user_Modificar_Ciiu_Nivel2(UpdateView):
    template_name = 'usuario/ciiu/ciiu_nivel2/nuevo_ciiu_nivel2.html'
    model = Ciiu_nivel2
    success_url = reverse_lazy('user_lista_ciiu_nivel2')
    form_class = Ciiu_nivel2Form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = 'user_modificar_ciiu_nivel2'
        context['titulo'] = 'Ciiu Nivel 2'
        context['crud'] = ' Modificar'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_ciiu_nivel2'
        context['action'] = 'update'
        return context

class user_Eliminar_Ciiu_Nivel2(DeleteView):
    template_name = 'usuario/ciiu/ciiu_nivel2/eliminar_ciiu_nivel2.html'
    model = Ciiu_nivel2
    success_url = reverse_lazy('user_lista_ciiu_nivel2')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = 'user_eliminar_ciiu_nivel2'
        context['titulo'] = 'Ciiu Nivel 2'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_ciiu_nivel2'
        return context

# VISTAS DEL MODULO CIIU OPERACIONAL
class user_Lista_Ciiu_Operacinal(ListView):
    template_name = 'usuario/ciiu/ciiu_operacional/lista_ciiu_operacional.html'
    context_object_name = 'ciiu_operacional'
    model = Ciiu_Operacinal

    def get_queryset(self):
        queryset = super().get_queryset()
        nombres = self.request.GET.get('nombres')
        descripcion = self.request.GET.get('descripcion')
        if nombres:
            queryset = queryset.filter(ciiu_operacional__contains=nombres)
        if descripcion:
            queryset = queryset.filter(descripcion__contains=descripcion)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Ciiu Operacional'
        context['rol'] = 'usuario'
        context['nuevo'] = 'user_nuevo_ciiu_operacional'
        context['volver'] = 'user_inicio_ciiu'
        context['query'] = self.request.GET.get("query") or ""
        return context

class user_Nuevo_Ciiu_Operacinal(CreateView):
    template_name = 'usuario/ciiu/ciiu_operacional/nuevo_ciiu_operacional.html'
    model = Ciiu_Operacinal
    success_url = reverse_lazy('user_lista_ciiu_operacinal')
    form_class = Ciiu_OperacinalForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Ciiu Operacional'
        context['crud'] = ' Agregar'
        context['action_save'] = 'user_nuevo_ciiu_operacional'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_ciiu_operacinal'
        context['action'] = 'add'
        return context

class user_Modificar_Ciiu_Operacinal(UpdateView):
    template_name = 'usuario/ciiu/ciiu_operacional/nuevo_ciiu_operacional.html'
    model = Ciiu_Operacinal
    success_url = reverse_lazy('user_lista_ciiu_operacinal')
    form_class = Ciiu_OperacinalForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = 'user_modificar_ciiu_operacional'
        context['titulo'] = 'Ciiu Operacional'
        context['crud'] = ' Modificar'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_ciiu_operacinal'
        context['action'] = 'update'
        return context

class user_Eliminar_Ciiu_Operacinal(DeleteView):
    template_name = 'usuario/ciiu/ciiu_operacional/eliminar_ciiu_operacional.html'
    model = Ciiu_Operacinal
    success_url = reverse_lazy('user_lista_ciiu_operacinal')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = 'user_eliminar_ciiu_operacional'
        context['titulo'] = 'Ciiu Operacional'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_ciiu_operacinal'
        return context


# VISTAS DEL MODULO CARGO
class user_Lista_Cargo(ListView):
    template_name = 'usuario/cargos/lista_cargo.html'
    context_object_name = 'cargos'
    model = Cargo

    def get_queryset(self):
        queryset = super().get_queryset()
        nombres = self.request.GET.get('nombres')
        if nombres:
            queryset = queryset.filter(nombre__contains=nombres)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Cargo'
        context['rol'] = 'usuario'
        context['nuevo'] = 'user_nuevo_cargo'
        context['volver'] = 'usuario_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class user_Nuevo_Cargo(CreateView):
    template_name = 'usuario/cargos/nuevo_cargo.html'
    model = Cargo
    success_url = reverse_lazy('user_lista_cargo')
    form_class = CargoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cargo'
        context['crud'] = ' Agregar'
        context['action_save'] = 'user_nuevo_cargo'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_cargo'
        context['action'] = 'add'
        return context

class user_Modificar_Cargo(UpdateView):
    template_name = 'usuario/cargos/nuevo_cargo.html'
    model = Cargo
    success_url = reverse_lazy('user_lista_cargo')
    form_class = CargoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = 'user_modificar_cargo'
        context['titulo'] = 'Cargo'
        context['crud'] = ' Modificar'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_cargo'
        context['action'] = 'add'
        return context

class user_Eliminar_Cargo(DeleteView):
    template_name = 'usuario/cargos/eliminar_cargo.html'
    model = Cargo
    success_url = reverse_lazy('user_lista_cargo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = 'user_eliminar_cargo'
        context['titulo'] = 'Cargo'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_cargo'
        return context

# VISTAS DEL MODULO ORIGEN
class user_Inicio_Orignes(TemplateView):
    template_name = "usuario/origen/modulos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Origen'
        context['rol'] = 'usuario'
        context['volver'] = 'usuario_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

# VISTAS DEL MODULO PAIS
class user_Lista_Pais(ListView):
    template_name = 'usuario/origen/pais/lista_pais.html'
    context_object_name = 'paises'
    model = Pais

    def get_queryset(self):
        queryset = super().get_queryset()
        nombres = self.request.GET.get('nombres')
        if nombres:
            queryset = queryset.filter(nombre__contains=nombres)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Pais'
        context['rol'] = 'usuario'
        context['nuevo'] = 'user_nuevo_pais'
        context['volver'] = 'user_inicio_origen'
        context['query'] = self.request.GET.get("query") or ""
        return context

class user_Nuevo_Pais(CreateView):
    template_name = 'usuario/origen/pais/nuevo_pais.html'
    model = Pais
    success_url = reverse_lazy('user_lista_pais')
    form_class = PaisForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Pais'
        context['crud'] = ' Agregar'
        context['action_save'] = 'user_nuevo_pais'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_pais'
        context['action'] = 'add'
        return context

class user_Modificar_Pais(UpdateView):
    template_name = 'usuario/origen/pais/nuevo_pais.html'
    model = Pais
    success_url = reverse_lazy('user_lista_pais')
    form_class = PaisForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = 'user_modificar_pais'
        context['titulo'] = 'Pais'
        context['crud'] = ' Modificar'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_pais'
        context['action'] = 'add'
        return context

class user_Eliminar_Pais(DeleteView):
    template_name = 'usuario/origen/pais/eliminar_pais.html'
    model = Pais
    success_url = reverse_lazy('user_lista_pais')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = 'user_eliminar_pais'
        context['titulo'] = 'Pais'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_pais'
        return context

# VISTAS DEL MODULO PROVINCIA
class user_Lista_Provincia(ListView):
    template_name = 'usuario/origen/provincia/lista_provincia.html'
    context_object_name = 'provincias'
    model = Provincia

    def get_queryset(self):
        queryset = super().get_queryset()
        nombres = self.request.GET.get('nombres')
        if nombres:
            queryset = queryset.filter(nombre__contains=nombres)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Provincia'
        context['rol'] = 'usuario'
        context['nuevo'] = 'user_nueva_provincia'
        context['volver'] = 'user_inicio_origen'
        context['query'] = self.request.GET.get("query") or ""
        return context

class user_Nuevo_Provincia(CreateView):
    template_name = 'usuario/origen/provincia/nueva_provincia.html'
    model = Provincia
    success_url = reverse_lazy('user_lista_provincia')
    form_class = ProvinciaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Provincia'
        context['crud'] = ' Agregar'
        context['action_save'] = 'user_nueva_provincia'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_provincia'
        context['action'] = 'add'
        return context

class user_Modificar_Provincia(UpdateView):
    template_name = 'usuario/origen/provincia/nueva_provincia.html'
    model = Provincia
    success_url = reverse_lazy('user_lista_provincia')
    form_class = ProvinciaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = 'user_modificar_provincia'
        context['titulo'] = 'Provincia'
        context['crud'] = ' Modificar'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_provincia'
        context['action'] = 'add'
        return context

class user_Eliminar_Provincia(DeleteView):
    template_name = 'usuario/origen/provincia/eliminar_provincia.html'
    model = Provincia
    success_url = reverse_lazy('user_lista_provincia')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = 'user_eliminar_provincia'
        context['titulo'] = 'Provincia'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_provincia'
        return context

# VISTAS DEL MODULO CIUDAD
class user_Lista_Ciudad(ListView):
    template_name = 'usuario/origen/ciudad/lista_ciudad.html'
    context_object_name = 'ciudades'
    model = Cuidad

    def get_queryset(self):
        queryset = super().get_queryset()
        nombres = self.request.GET.get('nombres')
        if nombres:
            queryset = queryset.filter(nombre__contains=nombres)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Ciudad'
        context['rol'] = 'usuario'
        context['nuevo'] = 'user_nueva_ciudad'
        context['volver'] = 'usuario_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class user_Nuevo_Ciudad(CreateView):
    template_name = 'usuario/origen/ciudad/nuevo_ciudad.html'
    model = Cuidad
    success_url = reverse_lazy('user_lista_ciudad')
    form_class = CuidadForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Ciudad'
        context['crud'] = ' Agregar'
        context['action_save'] = 'user_nueva_ciudad'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_ciudad'
        context['action'] = 'add'
        return context

class user_Modificar_Ciudad(UpdateView):
    template_name = 'usuario/origen/ciudad/nuevo_ciudad.html'
    model = Cuidad
    success_url = reverse_lazy('user_lista_ciudad')
    form_class = CuidadForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = 'user_modificar_ciudad'
        context['titulo'] = 'Ciudad'
        context['crud'] = ' Modificar'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_ciudad'
        context['action'] = 'add'
        return context

class user_Eliminar_Ciudad(DeleteView):
    template_name = 'usuario/origen/ciudad/eliminar_ciudad.html'
    model = Cuidad
    success_url = reverse_lazy('user_lista_ciudad')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = 'user_eliminar_ciudad'
        context['titulo'] = 'Ciudad'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_ciudad'
        return context

# VISTAS DEL MODULO ENTIDADES BANCARIAS
class user_Lista_Entidad(ListView):
    template_name = 'usuario/entidades_bancarias/lista_entidad.html'
    context_object_name = 'entidades'
    model = Entidad_Bancaria

    def get_queryset(self):
        queryset = super().get_queryset()
        nombres = self.request.GET.get('nombres')
        if nombres:
            queryset = queryset.filter(nombre__contains=nombres)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Entidades Bancarias'
        context['rol'] = 'usuario'
        context['nuevo'] = 'user_nueva_entidad'
        context['volver'] = 'usuario_modulos'  # Ajusté la ruta de retorno
        context['query'] = self.request.GET.get("query") or ""
        return context

class user_Nuevo_Entidad(CreateView):
    template_name = 'usuario/entidades_bancarias/nueva_entidad.html'
    model = Entidad_Bancaria
    success_url = reverse_lazy('user_lista_entidad')  # Ajusté la URL de éxito
    form_class = EntidadForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Entidad Bancaria'
        context['crud'] = ' Agregar'
        context['action_save'] = 'user_nueva_entidad'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_entidad'
        context['action'] = 'add'
        return context

class user_Modificar_Entidad(UpdateView):
    template_name = 'usuario/entidades_bancarias/nueva_entidad.html'
    model = Entidad_Bancaria
    success_url = reverse_lazy('user_lista_entidad')
    form_class = EntidadForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Entidad'
        context['crud'] = ' Modificar'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_entidad'
        context['action'] = 'add'
        return context

class user_Eliminar_Entidad(DeleteView):
    template_name = 'usuario/entidades_bancarias/eliminar_entidad.html'
    model = Entidad_Bancaria
    success_url = reverse_lazy('user_lista_entidad')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Entidad Bancaria'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_entidad'
        return context
# VISTAS DEL MODULO DE PERSONAS
class user_Lista_Persona(ListView):
    template_name = 'usuario/personas/lista_persona.html'
    context_object_name = 'personas'
    model = Persona

    def get_queryset(self):
        queryset = super().get_queryset()
        nombres = self.request.GET.get('nombres')
        if nombres:
            queryset = queryset.filter(nombre__contains=nombres)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Personas'
        context['rol'] = 'usuario'
        context['nuevo'] = 'user_nueva_persona'
        context['volver'] = 'usuario_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class user_Nuevo_Persona(CreateView):
    template_name = 'usuario/personas/nueva_persona.html'
    model = Persona
    success_url = reverse_lazy('user_lista_persona')
    form_class = PersonaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Persona'
        context['crud'] = ' Agregar'
        context['action_save'] = 'user_nueva_persona'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_persona'
        context['action'] = 'add'
        return context

class user_Modificar_Persona(UpdateView):
    template_name = 'usuario/personas/nueva_persona.html'
    model = Persona
    success_url = reverse_lazy('user_lista_persona')
    form_class = PersonaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Persona'
        context['crud'] = ' Modificar'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_persona'
        context['action'] = 'add'
        return context

class user_Eliminar_Persona(DeleteView):
    template_name = 'usuario/personas/eliminar_persona.html'
    model = Persona
    success_url = reverse_lazy('user_lista_persona')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Persona'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_persona'
        return context


# VISTAS DEL MODULO DE APALANCAMIENTO
class user_Lista_Apalancamiento(ListView):
    template_name = 'usuario/apalancamiento/lista_apalancamiento.html'
    context_object_name = 'apalancamiento'
    model = Apalancamiento

    def get_queryset(self):
        queryset = super().get_queryset()
        nombres = self.request.GET.get('nombres')
        if nombres:
            queryset = queryset.filter(nombre__contains=nombres)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Apalancamiento'
        context['rol'] = 'usuario'
        context['nuevo'] = 'user_nueva_apalancamiento'
        context['volver'] = 'usuario_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class user_Nuevo_Apalancamiento(CreateView):
    template_name = 'usuario/apalancamiento/nuevo_apalancamiento.html'
    model = Apalancamiento
    success_url = reverse_lazy('user_lista_apalancamiento')
    form_class = ApalancamientoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Apalancamiento'
        context['crud'] = ' Agregar'
        context['action_save'] = 'user_nueva_apalancamiento'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_apalancamiento'
        context['action'] = 'add'
        return context

class user_Modificar_Apalancamiento(UpdateView):
    template_name = 'usuario/apalancamiento/nuevo_apalancamiento.html'
    model = Apalancamiento
    success_url = reverse_lazy('user_lista_apalancamiento')
    form_class = ApalancamientoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Apalancamiento'
        context['crud'] = ' Modificar'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_apalancamiento'
        context['action'] = 'add'
        return context

class user_Eliminar_Apalancamiento(DeleteView):
    template_name = 'usuario/apalancamiento/eliminar_apalancamiento.html'
    model = Apalancamiento
    success_url = reverse_lazy('user_lista_apalancamiento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Apalancamiento'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_apalancamiento'
        return context


# VISTAS DEL MODULO DE ACCIONISTA
class user_Lista_Accionista(ListView):
    template_name = 'usuario/accionista/lista_accionista.html'
    context_object_name = 'accionista'
    model = Accionista

    def get_queryset(self):
        queryset = super().get_queryset()
        nombres = self.request.GET.get('nombres')
        if nombres:
            queryset = queryset.filter(nombre__contains=nombres)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Accionista'
        context['rol'] = 'usuario'
        context['nuevo'] = 'user_nuevo_accionista'
        context['volver'] = 'usuario_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class user_Nuevo_Accionista(CreateView):
    template_name = 'usuario/accionista/nuevo_accionista.html'
    model = Accionista
    success_url = reverse_lazy('user_lista_accionista')
    form_class = AccionistaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Accionista'
        context['crud'] = ' Agregar'
        context['action_save'] = 'user_nuevo_accionista'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_accionista'
        context['action'] = 'add'
        return context

class user_Modificar_Accionista(UpdateView):
    template_name = 'usuario/accionista/nuevo_accionista.html'
    model = Accionista
    success_url = reverse_lazy('user_lista_accionista')
    form_class = AccionistaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Accionista'
        context['crud'] = ' Modificar'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_accionista'
        context['action'] = 'add'
        return context

class user_Eliminar_Accionista(DeleteView):
    template_name = 'usuario/accionista/eliminar_accionista.html'
    model = Accionista
    success_url = reverse_lazy('user_lista_accionista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Accionista'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_accionista'
        return context

# VISTAS DEL MODULO DE JUNTAS
class user_Lista_Junta(ListView):
    template_name = 'usuario/junta_gerente/lista_junta_gerente.html'
    context_object_name = 'junta'
    model = Junta

    def get_queryset(self):
        queryset = super().get_queryset()
        nombres = self.request.GET.get('nombres')
        if nombres:
            queryset = queryset.filter(nombre__contains=nombres)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Persona de la Junta'
        context['rol'] = 'usuario'
        context['nuevo'] = 'user_nuevo_junta'
        context['volver'] = 'usuario_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class user_Nuevo_Junta(CreateView):
    template_name = 'usuario/junta_gerente/nuevo_junta_gerente.html'
    model = Junta
    success_url = reverse_lazy('user_lista_junta')
    form_class = JuntaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Persona de la Junta'
        context['crud'] = ' Agregar'
        context['action_save'] = 'user_nuevo_junta'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_junta'
        context['action'] = 'add'
        return context

class user_Modificar_Junta(UpdateView):
    template_name = 'usuario/junta_gerente/nuevo_junta_gerente.html'
    model = Junta
    success_url = reverse_lazy('user_lista_junta')
    form_class = JuntaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Persona de la Junta'
        context['crud'] = ' Modificar'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_junta'
        context['action'] = 'add'
        return context

class user_Eliminar_Junta(DeleteView):
    template_name = 'usuario/junta_gerente/eliminar_junta_gerente.html'
    model = Junta
    success_url = reverse_lazy('user_lista_junta')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Persona de la Junta'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_junta'
        return context


# VISTAS DEL MODULO DE Consejo directivo
class user_Lista_Consejo_directivo(ListView):
    template_name = 'usuario/consejo_directivo/lista_consejo_directivo.html'
    context_object_name = 'consejo_directivo'
    model = Consejo_directivo

    def get_queryset(self):
        queryset = super().get_queryset()
        nombres = self.request.GET.get('nombres')
        if nombres:
            queryset = queryset.filter(nombre__contains=nombres)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Persona del Consejo Directivo'
        context['rol'] = 'usuario'
        context['nuevo'] = 'user_nuevo_consejo_directivo'
        context['volver'] = 'usuario_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class user_Nuevo_Consejo_directivo(CreateView):
    template_name = 'usuario/consejo_directivo/nuevo_consejo_directivo.html'
    model = Consejo_directivo
    success_url = reverse_lazy('user_lista_consejo_directivo')
    form_class = Consejo_directivoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Persona del Consejo Directivo'
        context['crud'] = ' Agregar'
        context['action_save'] = 'user_nuevo_consejo_directivo'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_consejo_directivo'
        context['action'] = 'add'
        return context

class user_Modificar_Consejo_directivo(UpdateView):
    template_name = 'usuario/consejo_directivo/nuevo_consejo_directivo.html'
    model = Consejo_directivo
    success_url = reverse_lazy('user_lista_consejo_directivo')
    form_class = Consejo_directivoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Persona del Consejo Directivo'
        context['crud'] = ' Modificar'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_consejo_directivo'
        context['action'] = 'add'
        return context

class user_Eliminar_Consejo_directivo(DeleteView):
    template_name = 'usuario/consejo_directivo/eliminar_consejo_directivo.html'
    model = Consejo_directivo
    success_url = reverse_lazy('user_lista_consejo_directivo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Persona del Consejo Directivo'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_consejo_directivo'
        return context

class user_Auditores(TemplateView):
    template_name = "usuario/auditores/modulos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Auditores'
        context['rol'] = 'usuario'
        context['volver'] = 'usuario_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

# VISTAS DEL MODULO DE Auditor interno
class user_Lista_Auditor_interno(ListView):
    template_name = 'usuario/auditores/auditor_interno/lista_auditor_interno.html'
    context_object_name = 'auditor_interno'
    model = Auditor_interno

    def get_queryset(self):
        queryset = super().get_queryset()
        nombres = self.request.GET.get('nombres')
        if nombres:
            queryset = queryset.filter(nombre__contains=nombres)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Persona del Auditor interno'
        context['rol'] = 'usuario'
        context['nuevo'] = 'user_nuevo_auditor_interno'
        context['volver'] = 'usuario_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class user_Nuevo_Auditor_interno(CreateView):
    template_name = 'usuario/auditores/auditor_interno/nuevo_auditor_interno.html'
    model = Auditor_interno
    success_url = reverse_lazy('user_lista_auditor_interno')
    form_class = Auditor_internoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Persona del Auditor interno'
        context['crud'] = ' Agregar'
        context['action_save'] = 'user_nuevo_auditor_interno'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_auditor_interno'
        context['action'] = 'add'
        return context

class user_Modificar_Auditor_interno(UpdateView):
    template_name = 'usuario/auditores/auditor_interno/nuevo_auditor_interno.html'
    model = Auditor_interno
    success_url = reverse_lazy('user_lista_auditor_interno')
    form_class = Auditor_internoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Persona del Auditor interno'
        context['crud'] = ' Modificar'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_auditor_interno'
        context['action'] = 'add'
        return context

class user_Eliminar_Auditor_interno(DeleteView):
    template_name = 'usuario/auditores/auditor_interno/eliminar_auditor_interno.html'
    model = Auditor_interno
    success_url = reverse_lazy('user_lista_auditor_interno')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Persona del Auditor interno'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_auditor_interno'
        return context

# VISTAS DEL MODULO DE Auditor EXTERNO
class user_Lista_Auditor_externo(ListView):
    template_name = 'usuario/auditores/auditor_externo/lista_auditor_externo.html'
    context_object_name = 'auditor_externo'
    model = Auditor_externo

    def get_queryset(self):
        queryset = super().get_queryset()
        nombres = self.request.GET.get('nombres')
        if nombres:
            queryset = queryset.filter(nombre__contains=nombres)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Auditor externo'
        context['rol'] = 'usuario'
        context['nuevo'] = 'user_nuevo_auditor_externo'
        context['volver'] = 'usuario_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class user_Nuevo_Auditor_externo(CreateView):
    template_name = 'usuario/auditores/auditor_externo/nuevo_auditor_externo.html'
    model = Auditor_externo
    success_url = reverse_lazy('user_lista_auditor_externo')
    form_class = Auditor_externoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Auditor externo'
        context['crud'] = ' Agregar'
        context['action_save'] = 'user_nuevo_auditor_externo'
        context['rol'] = 'usuario'
        context['voler_login'] = 'login_usuario'
        context['volver'] = 'user_lista_auditor_externo'
        context['action'] = 'add'
        return context

class user_Modificar_Auditor_externo(UpdateView):
    template_name = 'usuario/auditores/auditor_externo/nuevo_auditor_externo.html'
    model = Auditor_externo
    success_url = reverse_lazy('user_lista_auditor_externo')
    form_class = Auditor_externoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Auditor externo'
        context['crud'] = ' Modificar'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_auditor_externo'
        context['action'] = 'add'
        return context

class user_Eliminar_Auditor_externo(DeleteView):
    template_name = 'usuario/auditores/auditor_externo/eliminar_auditor_externo.html'
    model = Auditor_externo
    success_url = reverse_lazy('user_lista_auditor_externo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Auditor externo'
        context['rol'] = 'usuario'
        context['voler_login'] = '/login_usuario'
        context['volver'] = '/user_lista_auditor_externo'
        return context

class user_Excel(TemplateView):
    template_name = "usuario/excel/subir_excel.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Subir excel'
        context['rol'] = 'Usuario'
        context['volver'] = 'usuario_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class user_Data_principal(TemplateView):
    template_name = "usuario/data_principal/lista_data_principal.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_usuario'
        context['titulo'] = 'Data Principal'
        context['rol'] = 'usuario'
        context['volver'] = 'usuario_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context
