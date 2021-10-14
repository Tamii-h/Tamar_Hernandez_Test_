from funciones_punto_11 import acumulador, par_impar, suma, resta, division, multiplicacion, par_impar, acumulador

menu = """                                          
        Menu
                    
    1- Suma.
    2- Resta.
    3- Division.
    4- Multiplicacion.
    5- pares e impares 
    6- acumulador
"""
print(menu)

opcion = 0   

while opcion != 6:                                                    
     opcion = int(input("Ingrese una opcion del menú: ")) 
     
     if opcion == 1:
        suma()
        
     elif opcion == 2:
        resta()
        
     elif opcion == 3:
        division()
        
     elif opcion == 4:
        multiplicacion()
        
     elif opcion == 5:
        par_impar()
     elif opcion == 6:
        acumulador()           