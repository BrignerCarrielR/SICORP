# Generated by Django 4.2.5 on 2023-10-31 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Principal', '0007_rename_id_cliente_permisos_id_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciiu_nivel2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciiu', models.TextField(blank=True, max_length=5)),
                ('descripcion', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'verbose_name': 'Ciiu Nivel 2',
                'verbose_name_plural': "Ciiu's Nivel 2",
                'ordering': ['id'],
            },
        ),
    ]
