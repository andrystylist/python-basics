from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import date
from enum import Enum, auto
from age import calculate_age

class Genero(Enum):
    MASCULINO = auto()
    FEMENINO = auto()

@dataclass
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
    nombre: str
    apellido: str
    genero: Genero
    fecha_nacimiento: str
    ser_vivo_tipo: str = field(default="Humano", init=False, repr=False)
    
    def obtener_edad(self, current_date=None) -> int:
        if current_date:
            return calculate_age(born_date=self.fecha_nacimiento_date, current_date=current_date)
        return calculate_age(born_date=self.fecha_nacimiento_date)
    
    @classmethod
    def get_ser_vivo_tipo(cls) -> str:
        return cls.ser_vivo_tipo

    @property
    def fecha_nacimiento_date(self) -> date:
        year, month, day = map(int, self.fecha_nacimiento.split("/")) # "1987/10/04"
        return date(year, month, day)

    @property
    def edad(self) -> int:
        return self.obtener_edad()
    
    def caminar(self) -> str:
        return f"{self.nombre} está caminando!"
    
    def correr(self) -> str:
        return f"{self.nombre} está corriendo!"

class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

@dataclass
class Empleado(Persona, Trabajador):
    salario: float
    departamento: str
    cargo: str

    def trabajar(self) -> str:
        return f"{self.nombre} está haciendo cosas de {self.cargo}"

    def caminar(self) -> str:
        return f"{self.nombre} está caminando como una empleada!"