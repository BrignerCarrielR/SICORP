from django.db import models

from PT_Consultoria.constantes import Opciones


motivos = Opciones()
GENERO = motivos.genero()

class Usuario(models.Model):
    nombres = models.CharField(max_length=50, blank=False, null=True )
    apellidos = models.CharField(max_length=50, blank=False, null=True )
    cedula = models.CharField(max_length=10, blank=False, null=True, unique=True)
    telefono = models.CharField(max_length=10, blank=False, null=True, unique=True)
    correo = models.CharField(max_length=50, blank=False, null=True, unique=True)
    genero = models.CharField(max_length=1, choices=GENERO, default=GENERO[0][0], blank=True, null=True)
    nom_user = models.CharField(max_length=15, blank=False, null=True, unique=True)
    contraseña = models.CharField(max_length=20, blank=False, null=False, unique=True)

    def to_json(self):
        return {'id': self.id, 'nombre': self.correo}

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['id']

    def __str__(self):
        return "{} {}".format(self.nombres, self.apellidos)