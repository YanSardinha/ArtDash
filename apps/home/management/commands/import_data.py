from django.core.management.base import BaseCommand
from django.db import connection
from django.db.models import Q
from ...models import dw_autor
from ...models import dw_artigos
import json
import re


class Command(BaseCommand):

    def __init__(self, *args, **options):
        super().__init__(*args, **options)
        self.connection = connection.cursor()
        self.json_data = json.load(open("C:/Users/yansa/OneDrive/Documentos/GitHub/ArtDash/dados_biblioteca_link_arquivos.json"))

    def handle(self, *args, **options):
        # Percorre o JSON
        for artigo in self.json_data:
            # Verifica se a lista de autores não está vazia
            if artigo["Autores"]:
                # Obtém o id do autor principal
                autor_id = self._get_autor_id(artigo["Autores"][0])

                # Cria um objeto do modelo de autor
                autor_obj = dw_autor.objects.get(id=autor_id)

                # Cria um objeto do modelo de artigo
                artigo_obj = dw_artigos(
                    titulo=artigo["Titulo"].replace("Ã‡", "ã").replace("Ã™", "õ"),
                    curso=artigo["NomeDoCurso"],
                    orientador=artigo["NomeOrientador"],
                    link=artigo["LinkArquivo"],
                    autores=autor_obj,
                )

                # Salva o artigo no banco de dados
                artigo_obj.save()

        # Fecha a conexão com o banco de dados
        connection.close()

    def _get_autor_id(self, autor):
        # Cria uma consulta SQL para encontrar o autor
        consulta = Q(tipo=autor["Tipo"], nome=autor["Nome"])

        # Executa a consulta
        autor_obj = dw_autor.objects.filter(consulta).first()

        # Se o autor não for encontrado, cria um novo objeto
        if not autor_obj:
            autor_obj = dw_autor(tipo=autor["Tipo"], nome=autor["Nome"])
            autor_obj.save()

        # Retorna o id do autor
        return autor_obj.id
