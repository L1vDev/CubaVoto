# Generated by Django 5.0.6 on 2024-06-17 21:02

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_nombre', models.CharField(max_length=50, verbose_name='Username')),
                ('user_apell', models.CharField(max_length=80, verbose_name='User_Apellidos')),
                ('user_ci', models.CharField(max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.MaxLengthValidator(11)], verbose_name='User_CI')),
                ('user_edad', models.IntegerField(verbose_name='User_Edad')),
                ('user_voto', models.BooleanField(default=False, verbose_name='User_Voto')),
                ('user_municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_Municipio', to='votation.municipio')),
                ('user_provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votation.provincia', verbose_name='User_Provincia')),
            ],
        ),
        migrations.AddField(
            model_name='municipio',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='municipios', to='votation.provincia'),
        ),
        migrations.CreateModel(
            name='Diputados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apell', models.CharField(max_length=80, verbose_name='Apellidos')),
                ('ci', models.CharField(max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.MaxLengthValidator(11)], verbose_name='CI')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('ocup', models.CharField(default='Sin Cargo', max_length=25, null=True, verbose_name='Ocupación')),
                ('descrip', models.TextField(blank=True, max_length=200, null=True, verbose_name='Descripción')),
                ('votos', models.IntegerField(verbose_name='Votos')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Municipio', to='votation.municipio')),
                ('provincia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votation.provincia', verbose_name='Provincia')),
            ],
        ),
    ]
