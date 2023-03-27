from django.db import models

# Create your models here.
class Trabajador(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    cedula = models.CharField(max_length=10, null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    f_nacimiento = models.DateField(null=False)
    direccion = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    estado = models.IntegerField(9, null=False)
    class Meta:
        db_table = 'Trabajador'

class Usuarios(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    usuario = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    estado = models.IntegerField(null=False)
    id_Trabajador = models.ForeignKey(Trabajador, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Usuarios'

class Pais(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    nombre = models.CharField(max_length=100)
    cedula = models.ForeignKey(Usuarios, null=False, blank=False, on_delete=models.CASCADE)
    image = models.BinaryField()

    class Meta:
        db_table = 'Pais'
