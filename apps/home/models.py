# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class dw_autor(models.Model):
  id = models.AutoField(primary_key=True)
  tipo = models.CharField(max_length=50)
  nome = models.CharField(max_length=100)


class dw_artigos(models.Model):
  id = models.AutoField(primary_key=True)
  titulo = models.CharField(max_length=255)
  curso = models.CharField(max_length=100)
  orientador = models.CharField(max_length=100)
  link = models.CharField(max_length=100)
  autores = models.ForeignKey('dw_autor', on_delete=models.CASCADE)