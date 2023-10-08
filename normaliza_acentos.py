import json

with open('C:/Users/Yan/teste/dados_biblioteca_link_arquivos.json', 'r', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)

def fix_encoding(text):
    return text.encode('latin-1').decode('utf-8')

for item in data:
    item["Titulo"] = fix_encoding(item["Titulo"])
    item["NomeDoCurso"] = fix_encoding(item["NomeDoCurso"])
    item["NomeOrientador"] = fix_encoding(item["NomeOrientador"])
    for autor in item["Autores"]:
        autor["Nome"] = fix_encoding(autor["Nome"])

with open('dados_normalizados_acento.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(data, arquivo_json, ensure_ascii=False, indent=4)
