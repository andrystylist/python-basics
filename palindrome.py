def main():
    frase = input('Ingrese su frase: ')

    if len(frase) == 0:
        print("Ingrese una frase con más caracteres")
        exit()
    elif len(frase) == 1:
        print("Es Palíndrome")
        exit()
    
    # Easy - Peace of cake
    # resultado = "Es Palíndrome"
    # if frase != frase[::-1]:
    #     resultado = "No es Palíndrome"
    
    # print(resultado)

    # Logica Positiva: Recomendable cuando un proceso se espera que falle cuando a penas una condición no se cumple
    resultado = 'Es palíndrome'
    j = len(frase) - 1
    for i in range(0, len(frase)//2):
        if frase[i] != frase[j]:
            resultado = 'No es Palíndrome'
            break
        j = j - 1
    
    # Logica Negativa: No recomendable cuando un proceso se espera que falle cuando a penas una condición no se cumple
    # resultado = "No es Palíndrome"
    # j = len(frase) - 1
    # for i in range(0, len(frase)//2):
    #     if frase[i] != frase[j]:
    #         break
    #     j = j - 1
    
    # if (i == (len(frase)//2)-1): # i completó el bucle, quiere decir que nunca entró en el if del break
    #     resultado = 'Es palíndrome'

    print(resultado)
        
if __name__ == "__main__":
    main()
