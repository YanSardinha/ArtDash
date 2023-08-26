# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import dw_artigos, dw_autor

# Register your models here.
@admin.register(dw_autor)
class dw_autor_admin(admin.ModelAdmin):
  list_display = ('id', 'tipo', 'nome')
  list_display_links = list_display
  list_per_page = 10
  list_filter = ('tipo', 'nome')

@admin.register(dw_artigos)
class dw_artigos_admin(admin.ModelAdmin):
  list_display = ('id', 'titulo', 'curso', 'orientador')
  list_display_links = list_display
  list_per_page = 10
  list_filter = ('titulo', 'curso', 'orientador')