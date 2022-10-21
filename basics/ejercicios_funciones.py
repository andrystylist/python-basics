#3 notas de un estudiante y decir la nota fina las dos primeras 30% y la ultima 40% 
"""""
def calcular_nota(n1, n2, n3):
    return(n1*0.3) + (n2*0.3) + (n3*0.4)

n1 = float(input('Ingrese la primera nota'))
n2 = float(input('Ingrese la segunda nota'))
n3 = float(input('Ingrese la tercera nota'))

nota_final = calcular_nota(n1, n2, n3)

print('La nota final del estudiante es:',nota_final)

# coloque float en la linea 4 despues de return y no me dejo hacer la multiplicacion 
"""""
#tabla de multiplicar

def tabla_multiplicar(n1, n2):
    return str(f"{n1} x {n2} = {n1*n2}") #practicar como colocar como string el mensaje y luego aplicar la operacion

n = int(input('ingrese el número entero:')) # para agregar el numero de la tabla que quiero que aparezca  

for i in range (0,11): #el condicional for es para que dentro de la variable i repita hasta el numero 10 la funcion
    print(tabla_multiplicar(n,i))
