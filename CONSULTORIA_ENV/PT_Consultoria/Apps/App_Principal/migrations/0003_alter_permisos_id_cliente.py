# Generated by Django 4.2.5 on 2023-10-12 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Usuario', '0002_remove_usuario_edad_usuario_cedula'),
        ('App_Principal', '0002_permisos_estado_permiso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permisos',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Usuario.usuario', unique=True),
        ),
    ]