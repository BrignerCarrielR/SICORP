# Generated by Django 4.1.13 on 2023-11-15 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Principal', '0021_alter_apalancamiento_activo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accionista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_endidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App_Principal.entidad_bancaria')),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App_Principal.persona')),
            ],
            options={
                'verbose_name': 'Accionista',
                'verbose_name_plural': 'Accionistas',
                'ordering': ['id_persona'],
            },
        ),
    ]
