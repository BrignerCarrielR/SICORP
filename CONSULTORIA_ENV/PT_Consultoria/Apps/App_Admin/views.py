from datetime import datetime,timezone

from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy

from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

from Apps.App_Admin.forms import PermisosForm, ModidicarPermisosForm
from Apps.App_Admin.models import Admin
from Apps.App_Principal.forms import Ciiu_nivel2Form, Ciiu_OperacinalForm, CargoForm, PaisForm,  ProvinciaForm, \
    CuidadForm, EntidadForm, PersonaForm, ApalancamientoForm, AccionistaForm, JuntaForm, Consejo_directivoForm, \
    Auditor_internoForm, Auditor_externoForm
from Apps.App_Principal.models import Permisos, Ciiu_nivel2, Ciiu_Operacinal, Cargo, Pais, Provincia, Cuidad, Entidad_Bancaria, \
    Persona, Apalancamiento, Accionista, Junta, Consejo_directivo, Auditor_interno, Auditor_externo
from Apps.App_Usuario.models import Usuario

def login_Admin(request):
    if request.method == 'POST':
        try:
            detalleAdmin = Admin.objects.get(nom_admin=request.POST['nom_admin'],
                                                 contraseña=request.POST['contraseña'])
            request.session['id'] = detalleAdmin.id
            request.session['nom_admin'] = detalleAdmin.nom_admin
            request.session['nombres'] = detalleAdmin.nombres
            request.session['correo'] = detalleAdmin.correo
            print(detalleAdmin.id)
            print(detalleAdmin.correo)

            return redirect('admin_modulos')
        except Admin.DoesNotExist as e:
            messages.success(request, 'Nombre de Usuario o Contraseña incorrecta..!')

    return render(request, 'administrador/login.html')

def CerrarSecionAdmin(request):
    try:
        del request.session['nom_admin']
    except:
        return render(request, 'inicio.html')
    return render(request, 'inicio.html')


class Recuperar_contrauser(TemplateView):
    template_name = "administrador/recuperar_contraseña.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            admin = Admin.objects.all()
            admin_list = list(admin.values())  # Convierte el QuerySet a lista de diccionarios
            context['admin_json'] = admin_list
            return context

class Modulos_Admin(TemplateView):
    template_name = "administrador/modulos.html"

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            permisos = Permisos.objects.all()
            fecha_actual=datetime.now()
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
            context['rol'] = 'administrador'
            context['voler_login'] = 'login_admin'
            return context


class Lista_Permiso(ListView):
    template_name = 'administrador/gestion_permisos/lista_permisos.html'
    context_object_name = 'permisos'
    model = Permisos

    def get_queryset(self):
        queryset = super().get_queryset()
        nombres = self.request.GET.get('nombres')
        fecha = self.request.GET.get('fecha')
        estado = self.request.GET.get('estado')
        if nombres:
            queryset = queryset.filter(id_usuario__nombres__contains=nombres)
        if fecha:
            queryset = queryset.filter(fecha_inicio__gt=fecha)
        if estado:
            queryset = queryset.filter(estado_permiso__contains=estado)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Permisos'
        context['rol'] = 'administrador'
        context['nuevo'] = 'nuevo_permiso'
        context['volver'] = 'admin_modulos'
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
        context['query'] = self.request.GET.get("query") or ""
        return context

class Nuevo_Permiso(CreateView):
    template_name = 'administrador/gestion_permisos/nuevo_permiso.html'
    model = Permisos
    success_url = reverse_lazy('lista_permiso')
    form_class = PermisosForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuarios= Usuario.objects.all()
        context['usuarios'] = usuarios
        context['titulo'] = 'Permisos'
        context['crud'] = ' Agregar'
        context['action_save'] = 'nuevo_permiso'
        context['rol'] = 'administrador'
        context['voler_login'] = 'login_admin'
        context['volver'] = 'lista_permiso'
        context['action'] = 'add'
        return context

class Modificar_Permiso(UpdateView):
    template_name = 'administrador/gestion_permisos/modificar_permiso.html'
    model = Permisos
    success_url = reverse_lazy('lista_permiso')
    form_class = ModidicarPermisosForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Permisos'
        context['crud'] = ' Modificar'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_permiso'
        context['action'] = 'add'
        return context

class Eliminar_Permiso(DeleteView):
    template_name = 'administrador/gestion_permisos/eliminar_permiso.html'
    model = Permisos
    success_url = reverse_lazy('lista_permiso')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Permisos'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_permiso'
        return context



class InicioTemplateView(TemplateView):
    template_name = "inicio.html"

class InicioCiiu(TemplateView):
    template_name = "administrador/ciiu/modulos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Ciiu'
        context['rol'] = 'administrador'
        context['volver'] = 'admin_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

# VISTAS DEL MODULO CIIU NIVEL2
class Lista_Ciiu_Nivel2(ListView):
    template_name = 'administrador/ciiu/ciiu_nivel2/lista_ciiu_nivel2.html'
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
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Ciiu Nivel 2'
        context['rol'] = 'administrador'
        context['nuevo'] = 'nuevo_ciiu_nivel2'
        context['volver'] = 'inicio_ciiu'
        context['query'] = self.request.GET.get("query") or ""
        return context

class Nuevo_Ciiu_Nivel2(CreateView):
    template_name = 'administrador/ciiu/ciiu_nivel2/nuevo_ciiu_nivel2.html'
    model = Ciiu_nivel2
    success_url = reverse_lazy('lista_ciiu_nivel2')
    form_class = Ciiu_nivel2Form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Ciiu Nivel 2'
        context['crud'] = ' Agregar'
        context['action_save'] = 'nuevo_ciiu_nivel2'
        context['rol'] = 'administrador'
        context['voler_login'] = 'login_admin'
        context['volver'] = 'lista_ciiu_nivel2'
        context['action'] = 'add'
        return context

class Modificar_Ciiu_Nivel2(UpdateView):
    template_name = 'administrador/ciiu/ciiu_nivel2/nuevo_ciiu_nivel2.html'
    model = Ciiu_nivel2
    success_url = reverse_lazy('lista_ciiu_nivel2')
    form_class = Ciiu_nivel2Form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Ciiu Nivel 2'
        context['crud'] = ' Modificar'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_ciiu_nivel2'
        context['action'] = 'add'
        return context

class Eliminar_Ciiu_Nivel2(DeleteView):
    template_name = 'administrador/ciiu/ciiu_nivel2/eliminar_ciiu_nivel2.html'
    model = Ciiu_nivel2
    success_url = reverse_lazy('lista_ciiu_nivel2')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Ciiu Nivel 2'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_ciiu_nivel2'
        return context

# VISTAS DEL MODULO CIIU OPERACIONAL
class Lista_Ciiu_Operacinal(ListView):
    template_name = 'administrador/ciiu/ciiu_operacional/lista_ciiu_operacional.html'
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
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Ciiu Operacional'
        context['rol'] = 'administrador'
        context['nuevo'] = 'nuevo_ciiu_operacinal'
        context['volver'] = 'inicio_ciiu'
        context['query'] = self.request.GET.get("query") or ""
        return context

class Nuevo_Ciiu_Operacinal(CreateView):
    template_name = 'administrador/ciiu/ciiu_operacional/nuevo_ciiu_operacional.html'
    model = Ciiu_Operacinal
    success_url = reverse_lazy('lista_ciiu_operacinal')
    form_class = Ciiu_OperacinalForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Ciiu Operacional'
        context['crud'] = ' Agregar'
        context['action_save'] = 'nuevo_ciiu_operacinal'
        context['rol'] = 'administrador'
        context['voler_login'] = 'login_admin'
        context['volver'] = 'lista_ciiu_operacinal'
        context['action'] = 'add'
        return context

class Modificar_Ciiu_Operacinal(UpdateView):
    template_name = 'administrador/ciiu/ciiu_operacional/nuevo_ciiu_operacional.html'
    model = Ciiu_Operacinal
    success_url = reverse_lazy('lista_ciiu_operacinal')
    form_class = Ciiu_OperacinalForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Ciiu Operacional'
        context['crud'] = ' Modificar'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_ciiu_operacinal'
        context['action'] = 'add'
        return context

class Eliminar_Ciiu_Operacinal(DeleteView):
    template_name = 'administrador/ciiu/ciiu_operacional/eliminar_ciiu_operacional.html'
    model = Ciiu_Operacinal
    success_url = reverse_lazy('lista_ciiu_operacinal')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Ciiu Operacional'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_ciiu_operacinal'
        return context

# VISTAS DEL MODULO CARGO
class Lista_Cargo(ListView):
    template_name = 'administrador/cargos/lista_cargo.html'
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
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Cargo'
        context['rol'] = 'administrador'
        context['nuevo'] = 'nuevo_cargo'
        context['volver'] = 'admin_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class Nuevo_Cargo(CreateView):
    template_name = 'administrador/cargos/nuevo_cargo.html'
    model = Cargo
    success_url = reverse_lazy('lista_cargo')
    form_class = CargoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cargo'
        context['crud'] = ' Agregar'
        context['action_save'] = 'nuevo_cargo'
        context['rol'] = 'administrador'
        context['voler_login'] = 'login_admin'
        context['volver'] = 'lista_cargo'
        context['action'] = 'add'
        return context

class Modificar_Cargo(UpdateView):
    template_name = 'administrador/cargos/nuevo_cargo.html'
    model = Cargo
    success_url = reverse_lazy('lista_cargo')
    form_class = CargoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Cargo'
        context['crud'] = ' Modificar'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_cargo'
        context['action'] = 'add'
        return context

class Eliminar_Cargo(DeleteView):
    template_name = 'administrador/cargos/eliminar_cargo.html'
    model = Cargo
    success_url = reverse_lazy('lista_cargo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Cargo'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_cargo'
        return context

# VISTAS DEL MODULO ORIGEN
class Inicio_Orignes(TemplateView):
    template_name = "administrador/origen/modulos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Origen'
        context['rol'] = 'administrador'
        context['volver'] = 'admin_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

# VISTAS DEL MODULO PAIS
class Lista_Pais(ListView):
    template_name = 'administrador/origen/pais/lista_pais.html'
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
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Pais'
        context['rol'] = 'administrador'
        context['nuevo'] = 'nuevo_pais'
        context['volver'] = 'inicio_origen'
        context['query'] = self.request.GET.get("query") or ""
        return context

class Nuevo_Pais(CreateView):
    template_name = 'administrador/origen/pais/nuevo_pais.html'
    model = Pais
    success_url = reverse_lazy('lista_pais')
    form_class = PaisForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Pais'
        context['crud'] = ' Agregar'
        context['action_save'] = 'nuevo_pais'
        context['rol'] = 'administrador'
        context['voler_login'] = 'login_admin'
        context['volver'] = 'lista_pais'
        context['action'] = 'add'
        return context

class Modificar_Pais(UpdateView):
    template_name = 'administrador/origen/pais/nuevo_pais.html'
    model = Pais
    success_url = reverse_lazy('lista_pais')
    form_class = PaisForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Pais'
        context['crud'] = ' Modificar'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_pais'
        context['action'] = 'add'
        return context

class Eliminar_Pais(DeleteView):
    template_name = 'administrador/origen/pais/eliminar_pais.html'
    model = Pais
    success_url = reverse_lazy('lista_pais')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Pais'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_pais'
        return context

# VISTAS DEL MODULO PROVINCIA
class Lista_Provincia(ListView):
    template_name = 'administrador/origen/provincia/lista_provincia.html'
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
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Provincia'
        context['rol'] = 'administrador'
        context['nuevo'] = 'nueva_provincia'
        context['volver'] = 'inicio_origen'
        context['query'] = self.request.GET.get("query") or ""
        return context

class Nuevo_Provincia(CreateView):
    template_name = 'administrador/origen/provincia/nueva_provincia.html'
    model = Provincia
    success_url = reverse_lazy('lista_provincia')
    form_class = ProvinciaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Provincia'
        context['crud'] = ' Agregar'
        context['action_save'] = 'nueva_provincia'
        context['rol'] = 'administrador'
        context['voler_login'] = 'login_admin'
        context['volver'] = 'lista_provincia'
        context['action'] = 'add'
        return context

class Modificar_Provincia(UpdateView):
    template_name = 'administrador/origen/provincia/nueva_provincia.html'
    model = Provincia
    success_url = reverse_lazy('lista_provincia')
    form_class = ProvinciaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Provincia'
        context['crud'] = ' Modificar'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_provincia'
        context['action'] = 'add'
        return context

class Eliminar_Provincia(DeleteView):
    template_name = 'administrador/origen/provincia/eliminar_provincia.html'
    model = Provincia
    success_url = reverse_lazy('lista_provincia')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Provincia'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_provincia'
        return context

# VISTAS DEL MODULO CIUDAD
class Lista_Ciudad(ListView):
    template_name = 'administrador/origen/ciudad/lista_ciudad.html'
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
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Ciudad'
        context['rol'] = 'administrador'
        context['nuevo'] = 'nueva_ciudad'
        context['volver'] = 'admin_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class Nuevo_Ciudad(CreateView):
    template_name = 'administrador/origen/ciudad/nuevo_ciudad.html'
    model = Cuidad
    success_url = reverse_lazy('lista_ciudad')
    form_class = CuidadForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Ciudad'
        context['crud'] = ' Agregar'
        context['action_save'] = 'nueva_ciudad'
        context['rol'] = 'administrador'
        context['voler_login'] = 'login_admin'
        context['volver'] = 'lista_ciudad'
        context['action'] = 'add'
        return context

class Modificar_Ciudad(UpdateView):
    template_name = 'administrador/origen/ciudad/nuevo_ciudad.html'
    model = Cuidad
    success_url = reverse_lazy('lista_ciudad')
    form_class = CuidadForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Cuidad'
        context['crud'] = ' Modificar'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_ciudad'
        context['action'] = 'add'
        return context

class Eliminar_Ciudad(DeleteView):
    template_name = 'administrador/origen/ciudad/eliminar_ciudad.html'
    model = Cuidad
    success_url = reverse_lazy('lista_ciudad')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Ciudad'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_ciudad'
        return context

# VISTAS DEL MODULO ENTIDADES BANCARIAS
class Lista_Entidad(ListView):
    template_name = 'administrador/entidades_bancarias/lista_entidad.html'
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
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Entidades Bancarias'
        context['rol'] = 'administrador'
        context['nuevo'] = 'nueva_entidad'
        context['volver'] = 'admin_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class Nuevo_Entidad(CreateView):
    template_name = 'administrador/entidades_bancarias/nueva_entidad.html'
    model = Entidad_Bancaria
    success_url = reverse_lazy('lista_entidad')
    form_class = EntidadForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Entidad Bancaria'
        context['crud'] = ' Agregar'
        context['action_save'] = 'nueva_entidad'
        context['rol'] = 'administrador'
        context['voler_login'] = 'login_admin'
        context['volver'] = 'lista_entidad'
        context['action'] = 'add'
        return context

class Modificar_Entidad(UpdateView):
    template_name = 'administrador/entidades_bancarias/nueva_entidad.html'
    model = Entidad_Bancaria
    success_url = reverse_lazy('lista_entidad')
    form_class = EntidadForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Entidad'
        context['crud'] = ' Modificar'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_entidad'
        context['action'] = 'add'
        return context

class Eliminar_Entidad(DeleteView):
    template_name = 'administrador/entidades_bancarias/eliminar_entidad.html'
    model = Entidad_Bancaria
    success_url = reverse_lazy('lista_entidad')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Entidad Bancaria'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_entidad'
        return context

# VISTAS DEL MODULO DE PERSONAS
class Lista_Persona(ListView):
    template_name = 'administrador/personas/lista_persona.html'
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
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Personas'
        context['rol'] = 'administrador'
        context['nuevo'] = 'nueva_persona'
        context['volver'] = 'admin_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class Nuevo_Persona(CreateView):
    template_name = 'administrador/personas/nueva_persona.html'
    model = Persona
    success_url = reverse_lazy('lista_persona')
    form_class = PersonaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Persona'
        context['crud'] = ' Agregar'
        context['action_save'] = 'nueva_persona'
        context['rol'] = 'administrador'
        context['voler_login'] = 'login_admin'
        context['volver'] = 'lista_persona'
        context['action'] = 'add'
        return context

class Modificar_Persona(UpdateView):
    template_name = 'administrador/personas/nueva_persona.html'
    model = Persona
    success_url = reverse_lazy('lista_persona')
    form_class = PersonaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Persona'
        context['crud'] = ' Modificar'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_persona'
        context['action'] = 'add'
        return context

class Eliminar_Persona(DeleteView):
    template_name = 'administrador/personas/eliminar_persona.html'
    model = Persona
    success_url = reverse_lazy('lista_persona')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Persona'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_persona'
        return context

# VISTAS DEL MODULO DE APALANCAMIENTO
class Lista_Apalancamiento(ListView):
    template_name = 'administrador/apalancamiento/lista_apalancamiento.html'
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
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Apalancamiento'
        context['rol'] = 'administrador'
        context['nuevo'] = 'nueva_apalancamiento'
        context['volver'] = 'admin_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class Nuevo_Apalancamiento(CreateView):
    template_name = 'administrador/apalancamiento/nuevo_apalancamiento.html'
    model = Apalancamiento
    success_url = reverse_lazy('lista_apalancamiento')
    form_class = ApalancamientoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Apalancamiento'
        context['crud'] = ' Agregar'
        context['action_save'] = 'nueva_apalancamiento'
        context['rol'] = 'administrador'
        context['voler_login'] = 'login_admin'
        context['volver'] = 'lista_apalancamiento'
        context['action'] = 'add'
        return context

class Modificar_Apalancamiento(UpdateView):
    template_name = 'administrador/apalancamiento/nuevo_apalancamiento.html'
    model = Apalancamiento
    success_url = reverse_lazy('lista_apalancamiento')
    form_class = ApalancamientoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Apalancamiento'
        context['crud'] = ' Modificar'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_apalancamiento'
        context['action'] = 'add'
        return context

class Eliminar_Apalancamiento(DeleteView):
    template_name = 'administrador/apalancamiento/eliminar_apalancamiento.html'
    model = Apalancamiento
    success_url = reverse_lazy('lista_apalancamiento')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Apalancamiento'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_apalancamiento'
        return context


# VISTAS DEL MODULO DE ACCIONISTA
class Lista_Accionista(ListView):
    template_name = 'administrador/accionista/lista_accionista.html'
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
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Accionista'
        context['rol'] = 'administrador'
        context['nuevo'] = 'nuevo_accionista'
        context['volver'] = 'admin_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class Nuevo_Accionista(CreateView):
    template_name = 'administrador/accionista/nuevo_accionista.html'
    model = Accionista
    success_url = reverse_lazy('lista_accionista')
    form_class = AccionistaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Accionista'
        context['crud'] = ' Agregar'
        context['action_save'] = 'nuevo_accionista'
        context['rol'] = 'administrador'
        context['voler_login'] = 'login_admin'
        context['volver'] = 'lista_accionista'
        context['action'] = 'add'
        return context

class Modificar_Accionista(UpdateView):
    template_name = 'administrador/accionista/nuevo_accionista.html'
    model = Accionista
    success_url = reverse_lazy('lista_accionista')
    form_class = AccionistaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Accionista'
        context['crud'] = ' Modificar'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_accionista'
        context['action'] = 'add'
        return context

class Eliminar_Accionista(DeleteView):
    template_name = 'administrador/accionista/eliminar_accionista.html'
    model = Accionista
    success_url = reverse_lazy('lista_accionista')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Accionista'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_accionista'
        return context

# VISTAS DEL MODULO DE JUNTAS
class Lista_Junta(ListView):
    template_name = 'administrador/junta_gerente/lista_junta_gerente.html'
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
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Persona de la Junta'
        context['rol'] = 'administrador'
        context['nuevo'] = 'nuevo_junta'
        context['volver'] = 'admin_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class Nuevo_Junta(CreateView):
    template_name = 'administrador/junta_gerente/nuevo_junta_gerente.html'
    model = Junta
    success_url = reverse_lazy('lista_junta')
    form_class = JuntaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Persona de la Junta'
        context['crud'] = ' Agregar'
        context['action_save'] = 'nuevo_junta'
        context['rol'] = 'administrador'
        context['voler_login'] = 'login_admin'
        context['volver'] = 'lista_junta'
        context['action'] = 'add'
        return context

class Modificar_Junta(UpdateView):
    template_name = 'administrador/junta_gerente/nuevo_junta_gerente.html'
    model = Junta
    success_url = reverse_lazy('lista_junta')
    form_class = JuntaForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Persona de la Junta'
        context['crud'] = ' Modificar'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_junta'
        context['action'] = 'add'
        return context

class Eliminar_Junta(DeleteView):
    template_name = 'administrador/junta_gerente/eliminar_junta_gerente.html'
    model = Junta
    success_url = reverse_lazy('lista_junta')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Persona de la Junta'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_junta'
        return context

# VISTAS DEL MODULO DE Consejo directivo
class Lista_Consejo_directivo(ListView):
    template_name = 'administrador/consejo_directivo/lista_consejo_directivo.html'
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
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Persona del Consejo Directivo'
        context['rol'] = 'administrador'
        context['nuevo'] = 'nuevo_consejo_directivo'
        context['volver'] = 'admin_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class Nuevo_Consejo_directivo(CreateView):
    template_name = 'administrador/consejo_directivo/nuevo_consejo_directivo.html'
    model = Consejo_directivo
    success_url = reverse_lazy('lista_consejo_directivo')
    form_class = Consejo_directivoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Persona del Consejo Directivo'
        context['crud'] = ' Agregar'
        context['action_save'] = 'nuevo_consejo_directivo'
        context['rol'] = 'administrador'
        context['voler_login'] = 'login_admin'
        context['volver'] = 'lista_consejo_directivo'
        context['action'] = 'add'
        return context

class Modificar_Consejo_directivo(UpdateView):
    template_name = 'administrador/consejo_directivo/nuevo_consejo_directivo.html'
    model = Consejo_directivo
    success_url = reverse_lazy('lista_consejo_directivo')
    form_class = Consejo_directivoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Persona del Consejo Directivo'
        context['crud'] = ' Modificar'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_consejo_directivo'
        context['action'] = 'add'
        return context

class Eliminar_Consejo_directivo(DeleteView):
    template_name = 'administrador/consejo_directivo/eliminar_consejo_directivo.html'
    model = Consejo_directivo
    success_url = reverse_lazy('lista_consejo_directivo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Persona del Consejo Directivo'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_consejo_directivo'
        return context

class Auditores(TemplateView):
    template_name = "administrador/auditores/modulos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Auditores'
        context['rol'] = 'administrador'
        context['volver'] = 'admin_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

# VISTAS DEL MODULO DE Auditor interno
class Lista_Auditor_interno(ListView):
    template_name = 'administrador/auditores/auditor_interno/lista_auditor_interno.html'
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
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Persona del Auditor interno'
        context['rol'] = 'administrador'
        context['nuevo'] = 'nuevo_auditor_interno'
        context['volver'] = 'admin_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class Nuevo_Auditor_interno(CreateView):
    template_name = 'administrador/auditores/auditor_interno/nuevo_auditor_interno.html'
    model = Auditor_interno
    success_url = reverse_lazy('lista_auditor_interno')
    form_class = Auditor_internoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Persona del Consejo Directivo'
        context['crud'] = ' Agregar'
        context['action_save'] = 'nuevo_auditor_interno'
        context['rol'] = 'administrador'
        context['voler_login'] = 'login_admin'
        context['volver'] = 'lista_auditor_interno'
        context['action'] = 'add'
        return context

class Modificar_Auditor_interno(UpdateView):
    template_name = 'administrador/auditores/auditor_interno/nuevo_auditor_interno.html'
    model = Auditor_interno
    success_url = reverse_lazy('lista_auditor_interno')
    form_class = Auditor_internoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Persona del Auditor interno'
        context['crud'] = ' Modificar'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_auditor_interno'
        context['action'] = 'add'
        return context

class Eliminar_Auditor_interno(DeleteView):
    template_name = 'administrador/auditores/auditor_interno/eliminar_auditor_interno.html'
    model = Auditor_interno
    success_url = reverse_lazy('lista_auditor_interno')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Persona del Auditor interno'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_auditor_interno'
        return context

# VISTAS DEL MODULO DE Auditor EXTERNO
class Lista_Auditor_externo(ListView):
    template_name = 'administrador/auditores/auditor_externo/lista_auditor_externo.html'
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
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Auditor externo'
        context['rol'] = 'administrador'
        context['nuevo'] = 'nuevo_auditor_externo'
        context['volver'] = 'admin_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context

class Nuevo_Auditor_externo(CreateView):
    template_name = 'administrador/auditores/auditor_externo/nuevo_auditor_externo.html'
    model = Auditor_externo
    success_url = reverse_lazy('lista_auditor_externo')
    form_class = Auditor_externoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Auditor externo'
        context['crud'] = ' Agregar'
        context['action_save'] = 'nuevo_auditor_externo'
        context['rol'] = 'administrador'
        context['voler_login'] = 'login_admin'
        context['volver'] = 'lista_auditor_externo'
        context['action'] = 'add'
        return context

class Modificar_Auditor_externo(UpdateView):
    template_name = 'administrador/auditores/auditor_externo/nuevo_auditor_externo.html'
    model = Auditor_externo
    success_url = reverse_lazy('lista_auditor_externo')
    form_class = Auditor_externoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Auditor externo'
        context['crud'] = ' Modificar'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_auditor_externo'
        context['action'] = 'add'
        return context

class Eliminar_Auditor_externo(DeleteView):
    template_name = 'administrador/auditores/auditor_externo/eliminar_auditor_externo.html'
    model = Auditor_externo
    success_url = reverse_lazy('lista_auditor_externo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['titulo'] = 'Auditor externo'
        context['rol'] = 'administrador'
        context['voler_login'] = '/login_admin'
        context['volver'] = '/lista_auditor_externo'
        return context

class Excel(TemplateView):
    template_name = "administrador/excel/subir_excel.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Subir excel'
        context['rol'] = 'administrador'
        context['volver'] = 'admin_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context



class Data_principal(TemplateView):
    template_name = "administrador/data_principal/lista_data_principal.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['voler_login'] = 'login_admin'
        context['titulo'] = 'Data Principal'
        context['rol'] = 'administrador'
        context['volver'] = 'admin_modulos'
        context['query'] = self.request.GET.get("query") or ""
        return context
