from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator

class Provincia(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE, related_name='municipios')

    def __str__(self):
        return self.nombre

class Diputados(models.Model):
    nombre=models.CharField(verbose_name="Nombre", max_length=50)
    apell=models.CharField(verbose_name="Apellidos", max_length=80)
    ci=models.CharField(verbose_name="CI", max_length=11, validators=[MinLengthValidator(11),MaxLengthValidator(11)], unique=True)
    edad=models.IntegerField(verbose_name="Edad")
    ocup=models.CharField(verbose_name="Ocupación", max_length=25, null=True, default="Sin Cargo")
    descrip=models.TextField(verbose_name="Descripción", max_length=200, null=True, blank=True)
    provincia=models.ForeignKey(Provincia, on_delete=models.CASCADE, verbose_name="Provincia")
    municipio=models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='Municipio')
    votos=models.IntegerField(verbose_name="Votos")

    def __str__(self):
        return self.nombre



class Persona(models.Model):
    user_nombre=models.CharField(verbose_name="Username", max_length=50)
    user_apell=models.CharField(verbose_name="User_Apellidos", max_length=80)
    user_ci=models.CharField(verbose_name="User_CI", max_length=11, validators=[MinLengthValidator(11),MaxLengthValidator(11)], unique=True)
    user_edad=models.IntegerField(verbose_name="User_Edad")
    user_provincia=models.ForeignKey(Provincia, on_delete=models.CASCADE, verbose_name="User_Provincia")
    user_municipio=models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='User_Municipio')
    user_voto=models.BooleanField(default=False, verbose_name="User_Voto")

    def __str__(self):
        return f"{self.nombre} {self.apell}"

class Admon():
    pass
