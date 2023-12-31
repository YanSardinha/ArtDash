# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models

# Create your models here.

class dw_autor(models.Model):
  id = models.AutoField(primary_key=True)
  tipo = models.CharField(max_length=50)
  nome = models.CharField(max_length=100)

  def __str__(self) -> str:
    return self.nome


class dw_artigos(models.Model):
  id = models.AutoField(primary_key=True)
  titulo = models.CharField(max_length=255)
  curso = models.CharField(max_length=100)
  orientador = models.CharField(max_length=100)
  link = models.CharField(max_length=100)
  autores = models.ForeignKey('dw_autor', on_delete=models.CASCADE)
  data_hora = models.DateTimeField(auto_now_add=True, editable=False)

  def __str__(self) -> str:
    return self.titulo