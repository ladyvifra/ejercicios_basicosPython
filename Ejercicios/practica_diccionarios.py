#Diccionarios
#Parecidas a listas y tuplas, pero se crea con clave:valor
#El orden es indiferente
midiccionario={"Alemania":"Berlín", "Francia":"Paris","Reino Unido":"Londres","Colombia":"Bogotá"}
print(midiccionario["Francia"])
print(midiccionario)
#agrgar más elementos
midiccionario["Italia"]="Lisboa"
print(midiccionario)
#modificar
midiccionario["Italia"]="Roma"
print(midiccionario)

#eliminar
del midiccionario["Reino Unido"]
print(midiccionario)

#se pueden crear diciconarios con tipos diferente
diccionario2={"Juan":3, "Pedro":5, "Raúl": 5}
print(diccionario2)

#Diccionario con tuplas
mitupla=["Mexico","Venezuela","Panamá","Argentina"]
diccionario3={mitupla[0]:"Ciudad de México", mitupla[1]:"Caracas", mitupla[2]: "Ciudad de Panamá", mitupla[3]: "Buenos Aires"}
print(diccionario3)
print(diccionario3["Mexico"])

diccionario4={23:"Jordan","Nombre":"Michael","Equipo":"Chicago","anillos":[1991,1992,1993,1996,1997,1998]}
print(diccionario4)
print(diccionario4["anillos"])

#devolver las claves
print(diccionario4.keys())
#devolver valore
print(diccionario4.values())
#la longitud del diccionario
print(len(diccionario4))
