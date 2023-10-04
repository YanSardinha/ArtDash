# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from .models import dw_artigos, dw_autor
import json
from django.db.models import Count
from django.core.serializers.json import DjangoJSONEncoder


def relatorio_quantidade_de_autores(request):
    quantidade = dw_autor.objects.count()
    return JsonResponse({'quantidade': quantidade})

    
def relatorio_quantidade_de_artigos(request):
    quantidade = dw_artigos.objects.count()
    return JsonResponse({'quantidade': quantidade})


def relatorio_quantidade_de_artigos_engenharia_civil(request):
    quantidade = dw_artigos.objects.filter(curso__icontains="civil").count()
    return JsonResponse({'quantidade': quantidade})


def lista_orientadores(request):
    artigos = dw_artigos.objects.all()
    orientadores = set(artigo.orientador for artigo in artigos)
    return JsonResponse(list(orientadores), safe=False)


def relatorio_artigos_por_orientador(request):
    orientadores = request.GET.get('orientadores', None)
    if orientadores is not None:
        orientadores = orientadores.split(',')
        artigos = dw_artigos.objects.filter(orientador__in=orientadores)
    else:
        artigos = dw_artigos.objects.all()

    relatorio = {}
    for artigo in artigos:
        if artigo.orientador in relatorio:
            relatorio[artigo.orientador] += 1
        else:
            relatorio[artigo.orientador] = 1

    data_json = {'data': list(relatorio.values()), 'labels': list(relatorio.keys())}
    return JsonResponse(data_json)


def relatorio_artigos_por_curso(request):
    # Agrupa os artigos por orientador e conta quantos artigos cada orientador tem
    data = dw_artigos.objects.values('curso').annotate(num_artigos=Count('curso'))

    # Converte os dados para o formato necessário para o gráfico
    cursos = [item['curso'] for item in data]
    num_artigos = [item['num_artigos'] for item in data]

    # Cria um dicionário para armazenar os dados
    context = {
        'cursos': cursos,
        'num_artigos': num_artigos,
    }

    # Retorna os dados como JSON
    return JsonResponse(context)


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]


        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))
