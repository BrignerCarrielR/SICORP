# Generated by Django 4.2.5 on 2023-10-12 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permisos',
            name='estado_permiso',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
