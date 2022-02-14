from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType



class Artista(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    def get_absolute_url(self):
        return reverse('artista-detalhes', args=[str(self.id)])

class Album(models.Model):
    nome = models.CharField(max_length=100)
    data_lancamento =  models.DateField()
    nota = models.IntegerField()
    def get_absolute_url(self):
        return reverse('album-detalhes', args=[str(self.id)])

class Musica(models.Model):
    artista = models.ForeignKey(Artista,on_delete=models.CASCADE)
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    data_lancamento =  models.DateField()
    nota = models.IntegerField()
    def get_absolute_url(self):
        return reverse('musica-detalhes', args=[str(self.id)])
