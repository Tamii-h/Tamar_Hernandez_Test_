resultado_operaciones = "\tℝesultado ="
num_1 = "Ingrese el primer numero a operar: "
num_2 = "Ingrese el segundo numero a operar: "


def suma():
    num1 = int(input(num_1))
    num2 = int(input(num_2))
    
    print(resultado_operaciones,num1+num2 ) 
    
    
def resta():
    num1 = int(input(num_1))
    num2 = int(input(num_2))
     
    print(resultado_operaciones ,num1-num2) 
    

def division():
    
    while True:
        try:
            dividendo = int(input("Ingrese el dividendo: "))
            divisor = int(input("Ingrese un divisor: "))
            cociente = dividendo / divisor
            
            print(f"El cociente de la division es: {cociente}")
            break
        except ZeroDivisionError:
            print("ZeroDivisionError: Debe ingresar un numero distinto de 0, vuelva a intentarlo.")
   

def multiplicacion():
    num1 = int(input("Ingrese el primer producto: "))
    num2 = int(input("Ingrese el segundo producto: "))
    
    print(resultado_operaciones,num1*num2) 
    

def par_impar():
    par = 0
    impar = 0
    pares = []
    impares = []
    contador = 0
    
    while (contador < 10):
        numero = int(input("Digite el numero: "))
        
        if numero % 2 == 0:
            par += 1
            pares.append(numero)
        else:
            impar += 1
            impares.append(numero)
        
        contador += 1
        
    print("Los numeros pares son:",pares)
    print("Los numeros impares son:",impares)
    
    
def acumulador():
    contador = 0
    
    while (contador < 6):
        num = int(input("Digite el numero a evaluar: "))
        
        if num > 0:
            print("El numero es mayor a 0.")
        elif num == 0:
            print("El numero ingresado es 0 vuelva a intentarlo")
        elif num < 0:
            print("El numero ingresado es menor a 0 vuelva a intentarlo")
        
        contador += 1 