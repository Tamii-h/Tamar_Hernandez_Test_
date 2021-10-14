# Inicio del programa 
def get_one(una_lista):
    for elemento in una_lista:
        return elemento
      
    
def get_elements(una_lista):
    for elemento in una_lista:
        yield elemento


if __name__ == "__main__":

    numeros = [1,2,3,4,5]

    devolución = get_one(numeros)

    print(devolución)


    resultado = list(get_elements(numeros))

    print(resultado)

# Fin del programa