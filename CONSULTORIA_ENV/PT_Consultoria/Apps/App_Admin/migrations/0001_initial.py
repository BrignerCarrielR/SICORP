# Generated by Django 4.2.5 on 2023-10-23 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50, null=True)),
                ('apellidos', models.CharField(max_length=50, null=True)),
                ('cedula', models.CharField(max_length=10, null=True, unique=True)),
                ('telefono', models.CharField(max_length=10, null=True, unique=True)),
                ('correo', models.CharField(max_length=50, null=True, unique=True)),
                ('genero', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Femenino')], default='M', max_length=1, null=True)),
                ('nom_admin', models.CharField(max_length=15, null=True, unique=True)),
                ('contraseña', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'Administrador',
                'verbose_name_plural': 'Administradores',
                'ordering': ['id'],
            },
        ),
    ]
