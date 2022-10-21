from datetime import date
# from classes import Persona, Genero
from mydataclass import Persona, Genero, Empleado

def main():
    print(Persona.ser_vivo_tipo)
    andry: Empleado = Empleado(
        nombre="Andry",
        apellido="Peña",
        genero=Genero.FEMENINO,
        fecha_nacimiento="1988/01/21",
        salario=5000000,
        departamento="Desarrollo",
        cargo="Mid Backend Developer"
    )
    andry.ser_vivo_tipo = "Mujer"

    # print(andry.trabajar())
    print(andry.caminar())

    gabriel: Empleado = Empleado(
        nombre="Jose Gabriel",
        apellido="Gonzalez",
        genero=Genero.MASCULINO,
        fecha_nacimiento="1987/10/04",
        salario=5000000,
        departamento="Desarrollo",
        cargo="Senior Frontend Developer"
    )

    gabriel_string = str(gabriel)

    # print(gabriel.trabajar())

    # print(dir(andry))
    # print(andry.nombre)
    # print(andry.apellido)
    # print(andry.genero)
    # print(andry.fecha_nacimiento)
    # print(andry.obtener_edad(current_date=date(2023, 2, 15)))
    # print(andry.obtener_edad())
    print(andry)
    print(gabriel)
    print(andry.edad)
    print(gabriel.edad)
    print(Persona.get_ser_vivo_tipo())

if __name__ == "__main__":
    main()
