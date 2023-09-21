import json
import html

with open('dados_biblioteca_link_arquivos.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

def corrigir_acentuacao(texto):
    return html.unescape(texto)

for i in data:
    i['Titulo'] = corrigir_acentuacao(i['Titulo'])
    # Corrigir outros campos conforme necessário
    print(i)
