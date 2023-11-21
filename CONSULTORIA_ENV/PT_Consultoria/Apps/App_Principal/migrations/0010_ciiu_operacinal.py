# Generated by Django 4.2.5 on 2023-10-31 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_Principal', '0009_alter_ciiu_nivel2_ciiu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciiu_Operacinal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciiu_operacional', models.CharField(blank=True, max_length=5)),
                ('descripcion', models.TextField(blank=True, max_length=500)),
                ('ciiu_nivel2', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='App_Principal.ciiu_nivel2')),
            ],
            options={
                'verbose_name': 'Ciiu Operacional',
                'verbose_name_plural': "Ciiu's Operacionales",
                'ordering': ['id'],
            },
        ),
    ]