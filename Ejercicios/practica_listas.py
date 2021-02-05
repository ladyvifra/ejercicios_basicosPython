milista=["María","Pepe","Marta", "Antonio"]

print(milista[:])
print(milista[2])
print(milista[-3])

#porción de lista
print(milista[0:3])
print(milista[:3])
print(milista[1:3])
print(milista[2:])

#Agregar un elelmto
milista.append("Sandra")
milista.insert(2,("Lucía"))
milista.extend(["Paolo", "Lucas"])

#Conocer el índice. Si está dos veces, nos devuelve la primera vez
print(milista.index("Marta"))


print(milista[:])

print("Pepe"in milista)

milista2=["Carlos", True, 3, "Lola"]

#borrar elementos
milista2.remove("Lola")
milista2.pop()#elimina el último elemento de la lista

milista3=milista+milista2
print(milista3[:])

#multiplicar listas
milista4=["Sandra", 5, False, "Gloria"]*3
print(milista4)


print