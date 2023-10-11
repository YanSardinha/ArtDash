from django.core.management.base import BaseCommand
from ...models import dw_autor
from ...models import dw_artigos
import json
from fuzzywuzzy import fuzz

class Command(BaseCommand):

    def __init__(self, *args, **options):
        super().__init__(*args, **options)
        self.json_data = self.load_json_file("C:/Users/Yan/Desktop/ArtDash/dados_normalizados_consolidados.json")

    def load_json_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as arquivo_json:
                return json.load(arquivo_json)
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR(f"Arquivo JSON não encontrado em '{file_path}'"))
            return []

    def handle(self, *args, **options):
        for artigo in self.json_data:
            titulo_normalizado = artigo["Titulo"]

            if artigo["Autores"]:
                autor_nome_normalizado = artigo["Autores"][0]["Nome"]

                autor_obj, created = dw_autor.objects.get_or_create(
                    tipo=artigo["Autores"][0]["Tipo"],
                    nome=autor_nome_normalizado
                )

                artigo_obj = dw_artigos(
                    titulo=titulo_normalizado,
                    curso=artigo["NomeDoCurso"],
                    orientador=artigo["NomeOrientador"],
                    link=artigo["LinkArquivo"],
                    autores=autor_obj,
                )

                artigo_obj.save()

        self.stdout.write(self.style.SUCCESS('Dados importados com sucesso!'))
