from django.db import models

# Create your models here.


class Cancion(models.Model):
    nom_cancion = models.CharField(max_length=30)
    desc_cancion = models.CharField(max_length=30)


    class Meta:
        verbose_name = "Cancion"
        verbose_name_plural = "Canciones"

    def __str__(self):
        return self.nom_cancion
