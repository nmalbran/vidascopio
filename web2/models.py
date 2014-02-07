from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Menu(models.Model):
    nombre = models.CharField(max_length=100)
    titulo = models.CharField(max_length=254)
    slug = models.CharField(max_length=50, unique=True)
    orden = models.IntegerField()

    class Meta:
        verbose_name = _('Menu')
        verbose_name_plural = _('Menus')
        ordering = ['orden']

    def __unicode__(self):
        return self.nombre


class Pagina(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.CharField(max_length=50, unique=True)
    menus = models.ManyToManyField('Menu')
    cita = models.TextField(blank=True, default='')
    autor_cita = models.CharField(max_length=100, default='', blank=True)
    texto = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = _('Pagina')
        verbose_name_plural = _('Paginas')

    def __unicode__(self):
        return self.titulo
