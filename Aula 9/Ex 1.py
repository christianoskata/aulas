# Crie um arquivo com o nome “grupo.txt”, nesse arquivo salve os nomes dos integrantes do seu grupo.

file = "grupo.txt"

membros = ["Carlos", "\nLucas", "\nDavinci", "\nKayo"]

arq = open(file, "w")

arq.writelines(membros)

arq.close()