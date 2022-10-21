from dataclasses import dataclass, field

@dataclass
class Persona:
    nombre: str
    apellido: str
    password: str = field(init=False, default="")
