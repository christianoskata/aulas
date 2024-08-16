import gerar_votos
import contar_votos

file = "votos.txt"
quantidade_votos = 25
quantidade_nulos = 5

gerar_votos.gerar_votos(quantidade_votos, quantidade_nulos, file)

# Lê os votos do arquivo
votos = contar_votos.ler_votos(file)

if votos is not None:
    # Apura os votos
    contagem_votos, votos_nulos = contar_votos.apurar_votos(votos)

    # Exibe os resultados da votação
    contar_votos.resultados_votacao(contagem_votos, votos_nulos)

else:
    print("Não foi localizado os votos")