# Generated by Django 5.2.1 on 2025-06-02 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('abreviatura', models.CharField(max_length=10, unique=True)),
                ('tipo', models.CharField(blank=True, choices=[('Licenciatura', 'Licenciatura'), ('Maestría', 'Maestría'), ('Doctorado', 'Doctorado')], max_length=50, null=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
                'ordering': ['nombre'],
            },
        ),
    ]
