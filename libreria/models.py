from django.db import models


# Create your models here.
class paciente(models.Model):
    rut_paciente=models.TextField(max_length=12, verbose_name='Rut')
    nombre_completo=models.TextField(max_length=100, verbose_name='Nombre')
    fecha_nacimiento=models.DateField
    telefono=models.IntegerField(verbose_name='Teléfono')
    direccion=models.TextField(max_length=300, verbose_name='Dirección')
    email=models.TextField(max_length=150, verbose_name='Email')
    contrasenia=models.TextField(max_length=150, verbose_name='Contrasenia')

def __str__(self):
    fila = "Rut: " + self.rut_paciente + " - " + "Nombre: " + self.nombre_completo + " - " + "" + self.fecha_nacimiento + " - " + "Teléfono: " + self.telefono + " - "  + "Dirección: " + self.direccion + " - " + "Email: " + self.email + " - " + "Contrasenia: " + self.contrasenia
    return fila