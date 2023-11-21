# Generated by Django 4.1.13 on 2023-11-15 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Principal', '0022_accionista'),
    ]

    operations = [
        migrations.CreateModel(
            name='Junta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_endidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App_Principal.entidad_bancaria')),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App_Principal.persona')),
            ],
            options={
                'verbose_name': 'Junta',
                'verbose_name_plural': 'Juntas',
                'ordering': ['id_persona'],
            },
        ),
    ]