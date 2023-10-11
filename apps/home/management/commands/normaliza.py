from django.core.management.base import BaseCommand
from django.db import connection
from django.db.models import Q
from ...models import dw_autor
from ...models import dw_artigos
import json


class Command(BaseCommand):

    def __init__(self, *args, **options):
        super().__init__(*args, **options)
        self.connection = connection.cursor()
        self.json_data = json.load(open("C:/Users/yansa/OneDrive/Documentos/GitHub/ArtDash/dados_biblioteca_link_arquivos.json"))

    def handle(self, *args, **options):
        for artigo in self.json_data:
            if artigo["Autores"]:
                autor_id = self._get_autor_id(artigo["Autores"][0])

                autor_obj = dw_autor.objects.get(id=autor_id)

                artigo_obj = dw_artigos(
                    titulo=artigo["Titulo"].replace("Ã‡", "ã"),
                    curso=artigo["NomeDoCurso"],
                    orientador=artigo["NomeOrientador"],
                    link=artigo["LinkArquivo"],
                    autores=autor_obj,
                )

                artigo_obj.save()

        connection.close()

    def _get_autor_id(self, autor):
        consulta = Q(tipo=autor["Tipo"], nome=autor["Nome"])

        autor_obj = dw_autor.objects.filter(consulta).first()

        if not autor_obj:
            autor_obj = dw_autor(tipo=autor["Tipo"], nome=autor["Nome"])
            autor_obj.save()

        return autor_obj.id
