# Tuplas- Listas inmutables. No se puede modifica(no append, extend, remove)
#Se puede comprobar si hay elementos en una tupla
#Ventajas: rápidas al ejecutar, menos espacio, formatean strings, se pueden usar como claves en un diciconario, las listas no lo hacen.

mitupla=("Juan", 13, 12, 1995)
print(mitupla[2])

#convertir tupla en lista
milista=list(mitupla)
print(milista)

lista1=["Pablo","Jorge","Luis",3]
tupla=tuple(lista1)
print(tupla)

#comprobar los elelmtos en la tupla
print("Juan"in mitupla)
#count-averugua cuántos elementos hay een una tupla
print(mitupla.count(13))

#saber la longitud d ela tupla
print(len(mitupla))

#se pueden crear tuplas unitarias
tupla2=("Juan",)
print(len(tupla2))
#se pueden crear tuplas sin préntesis, pero se recomienda ponerlos
tupla3="Pedro",13,2,1990
print(tupla3)
#desenpaquetar una tupla
nombre, dia, mes, agno=tupla3
print(nombre)
print(dia)
print(mes)
print(agno)



