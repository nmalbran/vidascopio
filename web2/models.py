from django.db import models

# Create your models here.

class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    slug = models.CharField(max_length=50, unique=True)
    orden = models.IntegerField()

    class Meta:
        verbose_name = _('Menu')
        verbose_name_plural = _('Menus')

    def __unicode__(self):
        return self.nombre


class Pagina(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.CharField(max_length=50, unique=True)
    menus = models.ManyToManyField()
    cita = models.TextField()
    autor_cita = models.CharField(max_length=100)
    texto = models.TextField()

    class Meta:
        verbose_name = _('Pagina')
        verbose_name_plural = _('Paginas')

    def __unicode__(self):
        return self.titulo
