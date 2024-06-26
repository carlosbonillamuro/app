# Generated by Django 4.0.2 on 2024-06-02 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rutas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rutas',
            name='viaje',
            field=models.CharField(default='None', max_length=10, verbose_name='No de viaje'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personal',
            name='cargo',
            field=models.CharField(choices=[('1', 'Maquinista'), ('2', 'Ayudante de Maquinista'), ('3', 'Garrotero')], max_length=1, verbose_name='Puesto'),
        ),
        migrations.AlterField(
            model_name='personal',
            name='empleado',
            field=models.CharField(max_length=20, verbose_name='No de empleado'),
        ),
        migrations.AlterField(
            model_name='personal',
            name='ingreso',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de ingreso'),
        ),
        migrations.AlterField(
            model_name='personal',
            name='licencia',
            field=models.CharField(max_length=20, verbose_name='No de licencia'),
        ),
        migrations.AlterField(
            model_name='personal',
            name='nombre',
            field=models.CharField(max_length=40, verbose_name='Nombre del trabajador'),
        ),
        migrations.AlterField(
            model_name='personal',
            name='segurosocial',
            field=models.CharField(max_length=11, verbose_name='No de Seguro Social'),
        ),
        migrations.AlterField(
            model_name='rutas',
            name='llegada',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Llegada'),
        ),
        migrations.AlterField(
            model_name='rutas',
            name='maquina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rutas.trenes', verbose_name='No de Maquina'),
        ),
        migrations.AlterField(
            model_name='rutas',
            name='maquinista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='rutas.personal', verbose_name='Capitan de viaje'),
        ),
        migrations.AlterField(
            model_name='rutas',
            name='salida',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Salida'),
        ),
        migrations.AlterField(
            model_name='trenes',
            name='idgps',
            field=models.CharField(max_length=10, verbose_name='ID del GPS'),
        ),
        migrations.AlterField(
            model_name='trenes',
            name='idmaquina',
            field=models.CharField(max_length=10, verbose_name='No de la Maquina'),
        ),
        migrations.AlterField(
            model_name='trenes',
            name='marca',
            field=models.CharField(max_length=15, verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='trenes',
            name='modelo',
            field=models.CharField(max_length=15, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='trenes',
            name='serie',
            field=models.CharField(max_length=20, verbose_name='No de serie'),
        ),
        migrations.AlterField(
            model_name='trenes',
            name='ubicacion',
            field=models.CharField(max_length=20, verbose_name='Ubicación'),
        ),
    ]
