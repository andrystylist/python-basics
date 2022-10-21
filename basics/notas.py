def calcular_nota(n1: float=0, n2: float=0, n3: float=0) -> float:
    """Esta funcion calcula la nota final a partir de tres nptas n1 (30%), n2 (30%) y n3 (40%)

    Args:
        n1 (float, optional): _description_. Defaults to 0.
        n2 (float, optional): _description_. Defaults to 0.
        n3 (float, optional): _description_. Defaults to 0.

    Returns:
        float: nota final
    """
    return (n1*0.3) + (n2*0.3) + (n3*0.4)

def main():
    nota1: float = float(input('Ingrese la primera nota '))
    nota2: float = float(input('Ingrese la segunda nota '))
    nota3: float = float(input('Ingrese la tercera nota '))

    nota_final: float = calcular_nota(n1=nota1, n2=nota2, n3=nota3) #estoy pasando nota1 al parametro n1...n2,n3

    resultado: str = 'Estas aprobado'
    if nota_final < 2.5:
        resultado = 'Repite año'

    print('La nota final del estudiante es:', nota_final)
    print(resultado)

if __name__ == "__main__":
    # lo que este dentro de este bloque solo se ejecuta cuando el archivo se ejecute directamente (python3 <nombre_archivo>)
    # y no cuando se importe este archivo desde otro modulo
    main()
