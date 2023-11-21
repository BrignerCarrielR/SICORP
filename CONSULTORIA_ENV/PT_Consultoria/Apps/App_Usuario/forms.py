from django import forms
from django.forms import ModelForm

from Apps.App_Usuario.models import Usuario


class UsuarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['autocomplete'] = 'off'

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if telefono and not telefono.isdigit() or len(telefono) != 10:
            raise forms.ValidationError('El teléfono debe contener exactamente 10 dígitos.')
        return telefono

    class Meta:
        model = Usuario
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter nombres'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter apellidos'}),
            'cedula': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter cedula'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'type': 'tel', 'placeholder': 'Enter telefono'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter correo'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'nom_user': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter nom_user'}),
            'contraseña': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter contraseña'}),
        }