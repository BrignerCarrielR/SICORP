# Generated by Django 4.2.5 on 2023-11-10 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Principal', '0015_alter_cargo_options_alter_ciiu_nivel2_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='entidad_bancaria',
            name='objeto_social',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
