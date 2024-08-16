import random
import os

def gerar_votos(quantidade_votos, quantidade_nulos, path):
    """Gera um arquivo de votos aleatórios com uma quantidade especificada de votos nulos."""
    # Definindo os códigos de identificação válidos
    candidatos = [1, 2, 3, 4, 5]

    # Calculando o número de votos válidos
    votos_validos = quantidade_votos - quantidade_nulos

    if votos_validos < 0:
        print("Erro: A quantidade de votos nulos não pode ser maior que a quantidade total de votos.")
        return

    # Gerando votos válidos aleatórios
    votos = [random.choice(candidatos) for _ in range(votos_validos)]
    """
    votos = []
    for _ in range(votos_validos):
        votos.append(random.choice(candidatos))
    """
    # Adicionando os votos nulos
    votos.extend(random.randint(6, 100) for _ in range(quantidade_nulos))

    # Embaralhando os votos para misturar os válidos e nulos
    random.shuffle(votos)

    # Escrevendo os votos no arquivo
    with open(path, 'w') as arquivo:
        for voto in votos:
            arquivo.write(f"{voto}\n")

    print(f"Arquivo '{path}' criado com {quantidade_votos} votos, incluindo {quantidade_nulos} votos nulos.")


if __name__ == "__main__":
    # Parâmetros para gerar os votos
    quantidade_votos = 100  # Quantidade total de votos
    quantidade_nulos = 10  # Quantidade de votos nulos
    caminho_arquivo = "votos.txt"

    if os.path.exists(caminho_arquivo):
        os.remove(caminho_arquivo)
        print(f"Arquivo {caminho_arquivo} apagado")
    else:
        pass
    # Gerar o arquivo de votos
    gerar_votos(quantidade_votos, quantidade_nulos, caminho_arquivo)
