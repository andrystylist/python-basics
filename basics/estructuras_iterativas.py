from datetime import datetime
import typing
# nombres: list[str] = ['Andry', 'Angel', 'Angely']

# nombres.append("Gabriel")
# nombres[1] = "Alejandro"

# for nombre in nombres:
#     print(f'Hola {nombre}! Cómo estás?')
#     # print('Hola {} y {}'.format(nombre, nombre))
#     # print('Hola ' + nombre)
#     # print('Hola', nombre)
#     # print('Hola %s %s'%(nombre, nombre))

# numeros_pares: tuple[int, ...] = (2, 4, 6, 8, 8)
# # numeros_pares[0] = 10 # error

# for numero_par in numeros_pares:
#     print(f'El doble de {numero_par} es {numero_par*2}')

# set_numeros_pares: set[int] = set(numeros_pares)
# numeros: set[int] = {1, 2, 3, 4, 5, 5, 4, 3, 18, 10}

# for numero in numeros:
#     print(f'{numero}')

# print(set_numeros_pares & numeros) # interception
# print(set_numeros_pares | numeros) # union
# print(set_numeros_pares - numeros) # left side
# print(numeros - set_numeros_pares) # rigth side

persona: dict[str, typing.Any] = {
    "nombre": "Maria",
    "apellido": "Marquez",
    "fecha_nacimiento": datetime.strptime("1992-07-22 07:00:45.000001", '%Y-%m-%d %H:%M:%S.%f')
}

# print(persona)
# print(persona["nombre"])
# print(persona.get("apellido"))
# https://www.geeksforgeeks.org/how-to-use-strptime-with-milliseconds-in-python/
# https://www.w3schools.com/python/python_datetime.asp
print(f'{persona.get("fecha_nacimiento"):%A %d %B, %Y}')

for key, value in persona.items():
    print(f"- {key.capitalize()} = {value}")

i = 0
while i < 10:
    i += 1
    print(i)
