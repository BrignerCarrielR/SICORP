# Generated by Django 4.2.5 on 2023-10-23 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Principal', '0006_alter_permisos_accionistas_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permisos',
            old_name='id_cliente',
            new_name='id_usuario',
        ),
    ]
