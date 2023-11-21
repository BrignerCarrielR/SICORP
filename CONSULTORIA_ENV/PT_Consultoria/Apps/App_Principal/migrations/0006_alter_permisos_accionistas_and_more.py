# Generated by Django 4.2.5 on 2023-10-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Principal', '0005_alter_permisos_ciu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permisos',
            name='accionistas',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='apalancamiento',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='auditores',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='cargos',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='con_directivo',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='data_principal',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='entidades',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='impuesto_causado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='junta',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='origen',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='permisos',
            name='personas',
            field=models.BooleanField(default=False),
        ),
    ]