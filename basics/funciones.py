from numero import suma, div
from models import Persona

def tabla_multiplicar(numero: int, saludo: str) -> None:
    print(saludo)
    for n in range(11):
        print(f"{n} x {numero} = {n*numero}")

print(__name__)
if __name__ == "__main__":
    tabla_multiplicar(saludo="Te voy joder si no me dices la tabla", numero=7)
    print(suma)
    print(div)
    andry: Persona = Persona(nombre="Andry", apellido="Peña")
    print(f"{andry}")
