from datetime import date
from enum import Enum, auto
from age import calculate_age

class Genero(Enum):
    MASCULINO = auto()
    FEMENINO = auto()

class Persona:
    """Clase Persona permite crear un objeto persona

        Attributes
        ----------
        nombre : str
            Representa el nombre de la persona
        apellido : str
            Representa el apellido de la persona
        generp : Genero
            Representa el género de la persona
        fecha_nacimiento : date
            Fecha de nacimiento de la persona

        Methods
        -------
        obtener_edad() -> int
            Returns the age of the person
    """
    ser_vivo_tipo: str = "Humano"

    def __init__(self, nombre: str, apellido: str, genero: Genero, fecha_nacimiento: str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero
        year, month, day = map(int, fecha_nacimiento.split("/")) # "1987/10/04"
        self.fecha_nacimiento = date(year, month, day)
    
    def obtener_edad(self, current_date=None) -> int:
        if current_date:
            return calculate_age(born_date=self.fecha_nacimiento, current_date=current_date)
        return calculate_age(born_date=self.fecha_nacimiento)
    
    @property
    def edad(self) -> int:
        return self.obtener_edad()

    def __repr__(self) -> str:
        return f"Persona(nombre={self.nombre}, apellido={self.apellido}, genero={self.genero}, fecha_nacimiento={self.fecha_nacimiento}, edad={self.edad})"
