from django.db import models

# Create your models here.

class Catalogo(models.Model):
    class Meta:
        verbose_name = 'Listado de Productos'

    nombre = models.CharField(max_lenght=20)

    def __str__(self):
        return self.nombre