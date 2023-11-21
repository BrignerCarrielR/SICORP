from django import forms
from django.forms import ModelForm

from Apps.App_Principal.models import Ciiu_nivel2, Ciiu_Operacinal, Cargo, Pais, Provincia, Cuidad, Entidad_Bancaria, \
    Persona, Apalancamiento, Accionista, Junta, Consejo_directivo, Auditor_externo, Auditor_interno


class Ciiu_nivel2Form(ModelForm):
    class Meta:
        model = Ciiu_nivel2
        fields = '__all__'
        widgets = {
            'ciiu': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'})
        }

class Ciiu_OperacinalForm(ModelForm):
    class Meta:
        model = Ciiu_Operacinal
        fields = '__all__'
        widgets = {
            'ciiu_operacional': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'ciiu_nivel2': forms.Select(attrs={'class': 'form-control'})
        }

class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingresa nombre del cargo'}),
        }

class PaisForm(ModelForm):
    class Meta:
        model = Pais
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingresa nombre del Pais'}),
        }

class ProvinciaForm(ModelForm):
    class Meta:
        model = Provincia
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingresa nombre de la Provincia'}),
            'id_pais': forms.Select(attrs={'class': 'form-control'})
        }

class CuidadForm(ModelForm):
    class Meta:
        model = Cuidad
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingresa nombre de la ciudad'}),
            'id_provincia': forms.Select(attrs={'class': 'form-control'})
        }

class EntidadForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Entidad_Bancaria
        fields = '__all__'
        widgets = {
            'no_identificacin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa nombre de la Empresa'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingresa nombre de la Empresa'}),
            'no_inscripcion': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Ingresa Numero de la '
                                                                                              'Inscripción'}),
            'fecha_inscripcion': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estado_permiso': forms.Select(attrs={'class': 'form-control'}),
            'id_ciudad': forms.Select(attrs={'class': 'form-control'}),
            'sector': forms.Select(attrs={'class': 'form-control'}),
            'sistema': forms.Select(attrs={'class': 'form-control'})
        }

class PersonaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
    class Meta:
        model = Persona
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa los nombres...'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingresa los apellidos...'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingresa su numero '
                                                                                     'identificación...'}),

        }

class ApalancamientoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
            self.fields['apalancamiento'].widget.attrs = {'readonly': True, 'class': 'form-control'}
    class Meta:
        model = Apalancamiento
        fields = '__all__'
        widgets = {
            'activo': forms.NumberInput(attrs={'class': 'form-control', 'value': '0'}),
            'patrimonio': forms.NumberInput(attrs={'class': 'form-control', 'value': '0'}),
            'apalancamiento': forms.TextInput(attrs={'class': 'form-control', 'value': '0', 'disabled': 'disabled'}),
        }

class AccionistaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
    class Meta:
        model = Accionista
        fields = '__all__'
        widgets = {
        }

class JuntaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
    class Meta:
        model = Junta
        fields = '__all__'
        widgets = {
        }

class Consejo_directivoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
    class Meta:
        model = Consejo_directivo
        fields = '__all__'
        widgets = {
            'fecha_asignacion': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class Auditor_externoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
    class Meta:
        model = Auditor_externo
        fields = '__all__'
        widgets = {
        }

class Auditor_internoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
    class Meta:
        model = Auditor_interno
        fields = '__all__'
        widgets = {
        }