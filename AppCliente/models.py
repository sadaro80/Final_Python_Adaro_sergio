from django.db import models



# Create your models here.

class usuario(models.Model):
    user = models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    tipo_user = models.CharField(max_length=20)
    fecha_registro = models.DateField()

    def __str__(self):
        return f"{self.user} ({self.email})"


class mensajes(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return f"Mensaje de {self.nombre} ({self.email})"