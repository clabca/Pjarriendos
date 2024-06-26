# Generated by Django 5.0.4 on 2024-05-10 17:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoPropiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='propiedades.region')),
            ],
        ),
        migrations.CreateModel(
            name='Propiedad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('m2_construidos', models.FloatField()),
                ('m2_terreno', models.FloatField()),
                ('num_estacionamientos', models.PositiveIntegerField()),
                ('num_habitaciones', models.PositiveIntegerField()),
                ('num_banos', models.PositiveIntegerField()),
                ('direccion', models.CharField(max_length=255)),
                ('comuna', models.CharField(max_length=100)),
                ('precio_arriendo_mensual', models.DecimalField(decimal_places=2, max_digits=10)),
                ('arrendador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('tipo_propiedad', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='propiedades.tipopropiedad')),
            ],
        ),
    ]
