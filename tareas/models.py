from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.


    
class Proveedor(models.Model):
    proveedor = models.CharField(max_length = 25)
        
    def __str__(self):
        return self.proveedor

class Producto(models.Model):
    proveedor = models.ForeignKey(Proveedor, null=True, on_delete=models.PROTECT)
    modelo = models.CharField(max_length=25)
    ficha_tecnica = models.FileField(upload_to='Chimeneas', null=True)
    
    def __str__(self):
        return self.modelo 


class Tarea (models.Model):
    titulo = models.CharField(max_length=100)
    cliente= models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    material = models.TextField(blank=True)
    creacion = models.DateTimeField(auto_now_add = True)
    completado= models.DateTimeField(null=True, blank=True)
    importante = models.BooleanField (default =True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, null = True, blank = True, on_delete = models.PROTECT)
    modelo = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    
    def __str__(self):
        return self.titulo + ' - Montador : ' + self.usuario.username


class ImagenTarea (models.Model):
    imagen = models.FileField (upload_to = "Chimeneas")
    tarea = models.ForeignKey(Tarea, on_delete = models.CASCADE, related_name='archivos')
    

      
