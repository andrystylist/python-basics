"""
     _summary_
     PEP8
"""
tiene_llave: str = input("Tienes una llave? ") # One line comments
mensaje_error: str = ""

if tiene_llave.upper() != "SI":
    mensaje_error = "No puede entrar"

if mensaje_error:
    print(f"Hola, {mensaje_error}")
    print("fin")
    exit()

forma: str = input("Qué forma tiene la llave? ").lower()
color: str = input("Qué color tiene la llave? ").lower()

mensaje: str = "Tiene la llave equivocada"
if forma == "cuadrada" and color == "naranja":
    mensaje = "Entra por puerta 1"
elif forma == "redonda" and color == "amarilla":
    mensaje = "Entra por puerta 2"
elif forma == "roja" and color == "triangular":
    mensaje = "Entra por puerta 3"

print(f"{mensaje}")
