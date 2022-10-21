from functools import cached_property
from typing import Callable

def suma(num1: float, num2: float) -> float:
    """Esto suma dos números float

    Args:
        num1 (float): el primero número
        num2 (float): el segundo número

    Returns:
        float: la suma de los dos números
    """
    return num1 + num2

# Closures: Ellas permiten retornar una función interna (a una function padre)
# y esa función interna tiene acceso al estado de su función padre
def get_saludo_emoji(persona: str):
    emoji: str = "😍"
    def saludo():
        return f"Hola {persona}! {emoji}"
    return saludo

# Assign a function to a variable
# mi_suma: Callable[[float, float], float] = suma
#print(mi_suma(num1=2.4, num2=6.6))

# Haciendo uso de un closure
# mi_saludo: callable = get_saludo_emoji(persona="Andry")
# print(mi_saludo())


# # Simple Decorator (No Params)
# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Something is happening before the function is called.")
#         sobrenombre = "Feita"
#         nombre = args[0] if len(args) > 0 else kwargs["name"]
#         func(f"{nombre} {sobrenombre}")
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_whee(name: str):
#     print(f"Whee {name}!")

# say_whee(name="Andry")

# say_hi = my_decorator(func=say_whee)
# say_hi()

# # factory de decorators
# def saludo_restringido(nombre: str):
#     def decorator(func: callable):
#         def wrapper():
#             if ("Andry" != nombre):
#                 func()
#             else:
#                 print("No quiero saludarte porque eres fea")
#         return wrapper
#     return decorator

# @saludo_restringido("Andry")
# def saludar():
#     print("Hola!")

# saludar()

def imprimir(*args):
    index: int = 1
    for text in args:
        print(f"{index}.- {text}")
        index += 1

imprimir(98)