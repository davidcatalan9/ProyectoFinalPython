# Generated by Django 4.2.3 on 2023-08-15 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profesores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=40)),
                ('ciudad', models.CharField(max_length=30)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='profesores.curso')),
                ('trabajos', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='profesores.trabajos')),
            ],
        ),
    ]
