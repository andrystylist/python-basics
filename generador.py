from socketserver import DatagramRequestHandler


def pares(limite):
    num = 0
    while num <= limite:
        if num%2 == 0:
            yield num
        num = num + 1

def main():
    print("---------- FOR ----------")
    for par in pares(10):
        print(par) # 0, 2, 4, 6, 8, 10
    
    print("---------- WHILE NEXT ----------")

    gen_pares = pares(10)
    while True:
        try:
            par = next(gen_pares)
            print(par)
        except StopIteration:
            break
        except:
            print("Error desconocido")

    
    # raise Exception("Se jodio esta vaina")

if __name__ == "__main__":
    main()
