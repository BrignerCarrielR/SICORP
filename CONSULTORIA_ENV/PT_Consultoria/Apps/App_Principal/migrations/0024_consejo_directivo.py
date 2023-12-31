# Generated by Django 4.1.13 on 2023-11-15 22:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Principal', '0023_junta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consejo_directivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodo', models.CharField(blank=True, choices=[('Indefinido', 'Indefinido'), ('Definido', 'Definido')], max_length=20, null=True)),
                ('fecha_inscripcion', models.DateField(null=True)),
                ('id_endidad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App_Principal.entidad_bancaria')),
                ('id_persona', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App_Principal.persona')),
            ],
            options={
                'verbose_name': 'Consejo directivo',
                'verbose_name_plural': 'Consejos directivos',
                'ordering': ['id_persona'],
            },
        ),
    ]
