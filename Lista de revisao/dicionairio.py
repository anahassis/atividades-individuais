# QUESTÃO 1
def contagem_caracteres(texto):
    contagem = {}
    for caractere in texto:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    return contagem

frase = "python programming"
resultado = contagem_caracteres(frase)
print(resultado)

# QUESTÃO 2


# QUESTÃO 3
def mesclar_dicionarios(dicionario1: dict, dicionario2: dict):
    dicionario_final = dicionario1
    for chave in dicionario2:
        if chave in dicionario_final:
            if dicionario2[chave] > dicionario_final[chave]:
                dicionario_final[chave] = dicionario2[chave]
        else:
            dicionario_final[chave] = dicionario2[chave]
    return dicionario_final

dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 4, 'd': 5}
resultado = mesclar_dicionarios(dicionario1, dicionario2)
print(resultado)

# QUESTÃO 4
def filtrar_dicionario(dados: dict, chaves_filtradas: list):
    dicionario_filtrado = {}
    for chave in chaves_filtradas:
        dicionario_filtrado[chave] = dados[chave]
    return dicionario_filtrado

dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves_filtradas = ['a', 'c', 'e']
resultado = filtrar_dicionario(dados, chaves_filtradas)
print(resultado)

# QUESTÃO 5
def resultado_votacao(lista_votos: list):
    votos_totais = {}
    total_votos = 0

    for urna in lista_votos:
        for candidato in urna:
            if candidato in votos_totais:
                votos_totais[candidato] += urna[candidato]
            else:
                votos_totais[candidato] = urna[candidato]
            total_votos += urna[candidato]

    for candidato in votos_totais:
        votos_totais[candidato] = (
            candidato,
            votos_totais[candidato] / total_votos * 100
        )

    return votos_totais

votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]

resultado = resultado_votacao(votos)
print(resultado)