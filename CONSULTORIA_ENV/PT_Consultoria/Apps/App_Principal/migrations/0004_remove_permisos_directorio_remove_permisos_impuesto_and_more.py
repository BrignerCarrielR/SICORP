# Generated by Django 4.2.5 on 2023-10-23 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Usuario', '0002_remove_usuario_edad_usuario_cedula'),
        ('App_Principal', '0003_alter_permisos_id_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permisos',
            name='directorio',
        ),
        migrations.RemoveField(
            model_name='permisos',
            name='impuesto',
        ),
        migrations.AddField(
            model_name='permisos',
            name='auditores',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='permisos',
            name='cargos',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='permisos',
            name='ciu',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='permisos',
            name='con_directivo',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='permisos',
            name='entidades',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='permisos',
            name='impuesto_causado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='permisos',
            name='junta',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='permisos',
            name='origen',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='permisos',
            name='personas',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='accionistas',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='apalancamiento',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='data_principal',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='estado_permiso',
            field=models.CharField(blank=True, choices=[('En Curso', 'En Curso'), ('Finalizado', 'Finalizado')], default='En Curso', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='id_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App_Usuario.usuario'),
        ),
    ]
