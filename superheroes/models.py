from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    founder = models.CharField(max_length=100, blank=True, default='')
    fecha = models.CharField(max_length=30, default=1/1/2000)
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Heroe(models.Model):
    name = models.CharField(max_length= 100, blank=True, default='')
    gender = models.CharField(max_length= 100, blank=True, default='')
    real_name = models.CharField(max_length= 100, blank=True, default='')
    publisher = models.ForeignKey(Publisher, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name






