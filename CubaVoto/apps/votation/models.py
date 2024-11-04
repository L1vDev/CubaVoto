from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager


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
    #ci=models.CharField(verbose_name="CI", max_length=11, validators=[MinLengthValidator(11),MaxLengthValidator(11)], primary_key=True)
    nombre=models.CharField(verbose_name="Nombre", max_length=200)
    age=models.IntegerField(verbose_name="Edad")
    cargo=models.CharField(verbose_name="Ocupación", max_length=100,blank=True, default="Sin Cargo")
    biografia=models.TextField(verbose_name="Descripción", max_length=3000, blank=True, default="Sin Descripcion")
    provincia=models.ForeignKey(Provincia, on_delete=models.CASCADE, verbose_name="Provincia")
    municipio=models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='Diputado')
    imagen = models.ImageField(verbose_name="Imagen", default="nopicture.jpg", upload_to="images/")
    votos=models.IntegerField(verbose_name="Votos", default=0, blank=True)

    def __str__(self):
        return self.nombre

class PersonaManager(BaseUserManager):
    def create_user(self, ci, nombre, edad, provincia, municipio, **extra_fields):#parametro password eliminado
        if not ci:
            raise ValueError('El CI debe ser establecido')
        
        user = self.model(
            ci=ci,
            nombre=nombre,
            edad=edad,
            provincia=provincia,
            municipio=municipio,
            **extra_fields
        )
        user.save(using=self._db)
        return user

    #parametro password eliminado
    def create_superuser(self, ci, nombre, edad, provincia, municipio, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser debe tener is_admin=True.')

        return self.create_user(ci, nombre, edad, provincia, municipio, **extra_fields)
    #parametro password eliminado
    

class Persona(AbstractBaseUser, PermissionsMixin):
    ci=models.CharField(verbose_name="CI", max_length=11, validators=[MinLengthValidator(11),MaxLengthValidator(11)], primary_key=True)
    nombre=models.CharField(verbose_name="Nombre", max_length=200)
    edad=models.IntegerField(verbose_name="Edad")
    provincia=models.ForeignKey(Provincia, on_delete=models.CASCADE, verbose_name="Provincia")
    municipio=models.ForeignKey(Municipio, on_delete=models.CASCADE, related_name='Persona')
    voto=models.BooleanField(default=False, verbose_name="Voto",blank=True)
    is_active = models.BooleanField(default=True)
    password=None
    last_login=None
    user_permissions=None
    groups=None
    USERNAME_FIELD='ci'
    REQUIRED_FIELDS=['nombre']

    
    objects = PersonaManager()

    def __str__(self):
        return f"{self.nombre}"

class Admon():
    pass
