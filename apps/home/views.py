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


        if load_template == 'chart-morris.html':
            # Busque os dados aqui
            cursos = dw_artigos.objects.values_list('curso', flat=True).distinct()
            dados = []

            for curso in cursos:
                artigos_por_orientador = dw_artigos.objects.filter(curso=curso).values('orientador').annotate(n=Count('id')).values('orientador', 'n')
                dado_curso = {'y': curso}
                for artigo in artigos_por_orientador:
                    dado_curso[artigo['orientador']] = artigo['n']
                dados.append(dado_curso)

            # Use Django's built-in JSON serializer to ensure your data is correctly formatted
            dados_json = json.dumps(dados, cls=DjangoJSONEncoder)

            context = {
                'dados': dados_json,
            }

            html_template = loader.get_template('home/chart-morris.html')
            return HttpResponse(html_template.render(context, request))
        

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))
