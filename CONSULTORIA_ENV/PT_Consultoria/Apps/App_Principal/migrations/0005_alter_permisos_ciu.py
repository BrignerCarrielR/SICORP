# Generated by Django 4.2.5 on 2023-10-23 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Principal', '0004_remove_permisos_directorio_remove_permisos_impuesto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permisos',
            name='ciu',
            field=models.BooleanField(default=False),
        ),
    ]
