# Crie um programa que vai receber uma lista de libs python,
# e irá salva-lás num arquivo “requirements.txt”.

libs = ["numpy", "\npandas", "\nrequests"]

file = "requirements.txt"

arq = open(file, "w")
arq.writelines(libs)

arq.close()