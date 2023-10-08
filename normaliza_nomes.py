import json
from fuzzywuzzy import fuzz

# Abra o arquivo JSON com os dados
with open('C:/Users/Yan/teste/dados_normalizados_acento.json', 'r', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)

# Função para encontrar orientadores semelhantes
def encontrar_orientadores_similares(data, limite_similaridade):
    orientadores_similares = {}

    for i in range(len(data)):
        orientador1 = data[i]["NomeOrientador"]
        for j in range(i + 1, len(data)):
            orientador2 = data[j]["NomeOrientador"]
            similaridade = fuzz.token_set_ratio(orientador1, orientador2)
            
            if similaridade >= limite_similaridade:
                if orientador1 not in orientadores_similares:
                    orientadores_similares[orientador1] = [orientador1]
                orientadores_similares[orientador1].append(orientador2)

    return orientadores_similares

# Encontrar orientadores similares com um limite de similaridade de 70
limite_similaridade = 70
orientadores_similares = encontrar_orientadores_similares(data, limite_similaridade)

# Normalizar os dados antes de salvá-los no arquivo JSON
for item in data:
    item["NomeOrientador"] = item["NomeOrientador"].lower()  # Normaliza para minúsculas

# Mapear nomes normalizados para o nome consolidado
mapeamento_nomes = {}
for grupo in orientadores_similares.values():
    nome_consolidado = grupo[0].lower()  # Usamos o primeiro nome como nome consolidado
    for nome in grupo:
        mapeamento_nomes[nome.lower()] = nome_consolidado

# Aplicar o mapeamento para consolidar os nomes nos dados normalizados
for item in data:
    item["NomeOrientador"] = mapeamento_nomes.get(item["NomeOrientador"], item["NomeOrientador"])

# Salvar os dados normalizados e consolidados em um arquivo JSON
with open('dados_normalizados_consolidados.json', 'w', encoding='utf-8') as arquivo_json:
    json.dump(data, arquivo_json, ensure_ascii=False, indent=4)

print(orientadores_similares)
print("Dados normalizados e consolidados salvos com sucesso no arquivo 'dados_normalizados_consolidados.json'.")
