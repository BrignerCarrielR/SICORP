from django import forms
from django.forms import ModelForm
from django.utils import timezone
from Apps.App_Principal.models import Permisos


class PermisosForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Establecer fecha de inicio como la fecha y hora actuales
        self.fields['fecha_inicio'].initial = timezone.now()

    def clean_fecha_fin(self):
        fecha_fin = self.cleaned_data.get('fecha_fin')

        # Verifica si la fecha de fin es mayor que la fecha y hora actuales
        if fecha_fin and fecha_fin <= timezone.now():
            raise forms.ValidationError('La fecha de fin debe ser mayor que la fecha y hora actuales.')

        return fecha_fin

    def clean(self):
        cleaned_data = super().clean()
        estado_permiso = cleaned_data.get('estado_permiso')
        id_usuario = cleaned_data.get('id_usuario')

        # Verifica si ya existe un permiso para el usuario
        usuario_tiene_permisos = Permisos.objects.filter(id_usuario=id_usuario).exists()

        if usuario_tiene_permisos:
            # Verifica si todos los permisos existentes están finalizados
            permisos_finalizados = Permisos.objects.filter(id_usuario=id_usuario, estado_permiso='Finalizado').count()

            if permisos_finalizados < Permisos.objects.filter(id_usuario=id_usuario).count():
                raise forms.ValidationError(
                    f'Todos los permisos existentes para el usuario {id_usuario} deben estar finalizados para agregar uno nuevo.')

    class Meta:
        model = Permisos
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'fecha_fin': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'id_usuario': forms.Select(attrs={'class': 'form-control'}),
        }

class ModidicarPermisosForm(ModelForm):

    class Meta:
        model = Permisos
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.TextInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'fecha_fin': forms.TextInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'id_usuario': forms.Select(attrs={'class': 'form-control'}),
        }