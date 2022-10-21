
mi_diccionario = {"a": 1, "b": 2, "c": 3, "d": 4, "a": 100}
print (mi_diccionario["a"])  #solo muestra el valor de a

mi_diccionario ['b'] = 6 #cambia el valor en el diccionario
print (mi_diccionario)

mi_diccionario ['e'] = 5 
print (mi_diccionario) # agrego el valor nuevo al diccionario

del mi_diccionario ["c"]
print (mi_diccionario)

print (mi_diccionario) #si agrego una clave identica en mi diccionario se ejecuta la ultima  izq a derech a=100 la otra no

valor = mi_diccionario.get ('a' , 'false')  #me va mostrar el valor de a si no estuviera daria false 
print (valor)

llaves = mi_diccionario.keys ()  #solo me muestra las llaves o claves a , b, d, e con el dictkeys 
print (llaves)

llaves = list (mi_diccionario.keys ()) #lista de llaves pura
print (llaves)

valores = list (mi_diccionario.values () ) # lista valores del diccionario 100,6,4 ...dentro de [] lista
print (valores)

valores = tuple (mi_diccionario.values () ) #tupla de valores me lo ejecuta con () por ser tuplA
print (valores)

diccionario2= { 'z': 23, 'w': 88} # une el segundo diccionario al primero 
mi_diccionario.update(diccionario2)
print (mi_diccionario)

