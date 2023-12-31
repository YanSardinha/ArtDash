# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('/teste', views.relatorio_artigos_por_orientador, name='relatorio_artigos_por_orientador'),
    path('lista_orientadores', views.lista_orientadores, name='lista_orientadores'),
    path('quantidade_artigos', views.relatorio_quantidade_de_artigos, name='relatorio_quantidade_de_artigos'),
    path('quantidade_artigos_civil', views.relatorio_quantidade_de_artigos_engenharia_civil, name="relatorio_quantidade_de_artigos_engenharia_civil"),
    path('quantidade_autores', views.relatorio_quantidade_de_autores, name='relatorio_quantidade_de_autores'),
    path('relatorio_artigos_por_curso', views.relatorio_artigos_por_curso, name='relatorio_artigos_por_curso'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
