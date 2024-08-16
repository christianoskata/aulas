
"""
arq = open("nomes.txt", "r")


print(lines)
for line in lines:
    print(line)
"""

arq = open("nomes.txt", "w")
arq.write("\nComando write")
arq.close()














import json

path = "teste.txt"
arq = open(path, 'w')
nomes = {
    "1": "Carlos",
    "2": "Joana",
}

json.dump(nomes, arq, indent=4)
