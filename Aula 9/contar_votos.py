import os

# Dicionário com os candidatos e seus códigos de identificação
candidatos = {
    1: "Bart",
    2: "Homer",
    3: "Krusty",
    4: "Mr Burns",
    5: "Ned Flanders"
}

def ler_votos(path):
    """Lê os votos do arquivo 'votos.txt' e retorna uma lista de votos."""
    with open(path, 'r') as arquivo:
        votos = [int(linha.strip()) for linha in arquivo.readlines()]
    return votos

def apurar_votos(votos):
    """Apura os votos, contando os votos para cada candidato e os votos nulos."""
    # Inicializa o contador de votos para cada candidato
    contagem_votos = {codigo: 0 for codigo in candidatos.keys()}
    votos_nulos = 0
    # Contabiliza os votos
    for voto in votos:
        if voto in contagem_votos:
            contagem_votos[voto] += 1
        else:
            votos_nulos += 1

    return contagem_votos, votos_nulos


def resultados_votacao(contagem_votos, votos_nulos):
    """Exibe os resultados da votação."""
    # Candidato mais votado
    mais_votado = max(contagem_votos, key=contagem_votos.get)
    # Candidato menos votado
    menos_votado = min(contagem_votos, key=contagem_votos.get)

    print(
        f"Candidato mais votado: {candidatos[mais_votado]} (Código: {mais_votado}) com {contagem_votos[mais_votado]} votos")
    print(
        f"Candidato menos votado: {candidatos[menos_votado]} (Código: {menos_votado}) com {contagem_votos[menos_votado]} votos")
    print(f"Total de votos nulos: {votos_nulos}")


if __name__ == "__main__":
    caminho_arquivo = "votos.txt"

    # Lê os votos do arquivo
    votos = ler_votos(caminho_arquivo)

    if votos is not None:
        # Apura os votos
        contagem_votos, votos_nulos = apurar_votos(votos)

        # Exibe os resultados da votação
        resultados_votacao(contagem_votos, votos_nulos)
