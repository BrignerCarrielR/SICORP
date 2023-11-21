from django.db import models
from Apps.App_Usuario.models import Usuario

from PT_Consultoria.constantes import Opciones

from PT_Consultoria.constantes import Opciones


motivos = Opciones()
GENERO = motivos.genero()
ESTADOPER = motivos.estadoPermiso()
ESTADOEN = motivos.estado_entidad()
SECTOR = motivos.sector()
SISTEMA = motivos.sistema()
PERIODO = motivos.perido()


class Permisos(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(blank=False, null=True)
    fecha_fin = models.DateTimeField(blank=False, null=True)
    con_directivo = models.BooleanField(default=False)
    personas = models.BooleanField(default=False)
    data_principal = models.BooleanField(default=False)
    accionistas = models.BooleanField(default=False)
    junta = models.BooleanField(default=False)
    cargos = models.BooleanField(default=False)
    origen = models.BooleanField(default=False)
    impuesto_causado = models.BooleanField(default=False)
    entidades = models.BooleanField(default=False)
    auditores = models.BooleanField(default=False)
    apalancamiento = models.BooleanField(default=False)
    excel = models.BooleanField(default=False)
    ciu = models.BooleanField(default=False) 

    estado_permiso = models.CharField(max_length=10, choices=ESTADOPER, default=ESTADOPER[0][1], blank=True, null=True)

    class Meta:
        verbose_name = "Permiso"
        verbose_name_plural = "Permisos"
        ordering = ['id']

    def __str__(self):
        return "{}".format(self.id_usuario)

class Ciiu_nivel2(models.Model):
    ciiu=models.CharField(max_length=5,blank=False, null=True)
    descripcion=models.TextField(max_length=500,blank=False, null=True)

    class Meta:
        verbose_name = "Ciiu Nivel 2"
        verbose_name_plural = "Ciiu's Nivel 2"
        ordering = ['ciiu']

    def __str__(self):
        return "{}".format(self.ciiu)

class Ciiu_Operacinal(models.Model):
    ciiu_operacional=models.CharField(max_length=20,blank=True, null=False)
    ciiu_nivel2=models.ForeignKey(Ciiu_nivel2, on_delete=models.PROTECT)
    descripcion=models.TextField(max_length=500,blank=True, null=False)

    class Meta:
        verbose_name = "Ciiu Operacional"
        verbose_name_plural = "Ciiu's Operacionales"
        ordering = ['ciiu_operacional']

    def __str__(self):
        return "{}".format(self.ciiu_operacional)

class Cargo (models.Model):
    nombre=models.CharField(max_length=50, blank=True, null=False)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"
        ordering = ['nombre']

    def __str__(self):
        return "{}".format(self.nombre)

class Pais(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=False)

    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
        ordering = ['nombre']

    def __str__(self):
        return "{}".format(self.nombre)

class Provincia(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=False)
    id_pais = models.ForeignKey(Pais, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"
        ordering = ['nombre']

    def __str__(self):
        return "{}".format(self.nombre)

class Cuidad(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=False)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Cuidad"
        verbose_name_plural = "Ciudades"
        ordering = ['nombre']

    def __str__(self):
        return "{}".format(self.nombre)

class Entidad_Bancaria(models.Model):
    no_identificacin = models.CharField(max_length=20, blank=True, null=False)
    nombre=models.CharField(max_length=100, blank=True, null=False)
    no_inscripcion = models.CharField(max_length=20, blank=True, null=False)
    fecha_inscripcion = models.DateField(blank=False, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOEN, blank=True, null=True)
    id_ciudad = models.ForeignKey(Cuidad, on_delete=models.PROTECT)
    sector = models.CharField(max_length=20, choices=SECTOR, blank=True, null=True)
    sistema = models.CharField(max_length=20, choices=SISTEMA, blank=True, null=True)
    ciiu_operacional = models.ForeignKey(Ciiu_Operacinal, on_delete=models.PROTECT)
    capital_suscrito = models.FloatField(blank=True, null=False)
    capital_autorizado = models.FloatField(blank=True, null=False)
    valor_nominal = models.FloatField(blank=True, null=False)
    objeto_social = models.TextField(max_length=500, blank=True, null=False)

    class Meta:
        verbose_name = "Endidad Bancaria"
        verbose_name_plural = "Endidades Bancarias"
        ordering = ['nombre']

    def __str__(self):
        return "{}".format(self.nombre)

class Persona(models.Model):
    nombres = models.CharField(max_length=100, blank=True, null=False)
    apellidos = models.CharField(max_length=100, blank=True, null=False)
    cedula = models.CharField(max_length=10, blank=True, null=False)
    id_pais = models.ForeignKey(Pais, on_delete=models.PROTECT)
    id_cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT, related_name='personas_cargo')
    id_cargo_2 = models.ForeignKey(Cargo, on_delete=models.PROTECT, blank=True, null=True,
                                   related_name='personas_cargo_2')
    genero = models.CharField(max_length=20, choices=GENERO, blank=True, null=True)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        ordering = ['nombres']

    def __str__(self):
        return "{} {}".format(self.nombres, self.apellidos)

class Apalancamiento(models.Model):
    entidad = models.ForeignKey(Entidad_Bancaria, on_delete=models.PROTECT)
    activo = models.FloatField(blank=True, null=False, default=0)
    patrimonio = models.FloatField(blank=True, null=False, default=0)
    apalancamiento = models.FloatField(blank=True, null=False, default=0)

    class Meta:
        verbose_name = "Apalancamiento"
        verbose_name_plural = "Apalancamientos"
        ordering = ['entidad']

    def __str__(self):
        return "{} - {}".format(self.entidad, self.apalancamiento)

class Accionista(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    id_endidad = models.ForeignKey(Entidad_Bancaria, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Accionista"
        verbose_name_plural = "Accionistas"
        ordering = ['id_persona']

    def __str__(self):
        return "{} - {}".format(self.id_persona, self.id_endidad)

class Junta(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    id_endidad = models.ForeignKey(Entidad_Bancaria, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Junta"
        verbose_name_plural = "Juntas"
        ordering = ['id_persona']

    def __str__(self):
        return "{} - {}".format(self.id_persona, self.id_endidad)

class Consejo_directivo(models.Model):
    id_persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    id_endidad = models.ForeignKey(Entidad_Bancaria, on_delete=models.PROTECT)
    periodo = models.CharField(max_length=20, choices=PERIODO, blank=True, null=True)
    fecha_asignacion = models.DateField(blank=False, null=True)

    class Meta:
        verbose_name = "Consejo directivo"
        verbose_name_plural = "Consejos directivos"
        ordering = ['id_persona']

    def __str__(self):
        return "{} - {}".format(self.id_persona, self.id_endidad)

class Auditor_interno(models.Model):
    empresa= models.CharField(max_length=20,blank=False, null=True)
    id_persona = models.ForeignKey(Persona, on_delete=models.PROTECT)
    id_endidad = models.ForeignKey(Entidad_Bancaria, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Auditor Interno"
        verbose_name_plural = "Auditores Internos"
        ordering = ['id_persona']

    def __str__(self):
        return "{} - {}".format(self.id_persona, self.id_endidad)

class Auditor_externo(models.Model):
    empresa = models.CharField(max_length=20, blank=False, null=True)
    id_endidad = models.ForeignKey(Entidad_Bancaria, on_delete=models.PROTECT)
    nombrefirma = models.CharField(max_length=20,blank=False, null=True)

    class Meta:
        verbose_name = "Auditor Externo"
        verbose_name_plural = "Auditores Externos"
        ordering = ['nombrefirma']

    def __str__(self):
        return "{} - {}".format(self.nombrefirma, self.id_endidad)