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
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
