# Este ejercicio tiene como fin el restar dos numeros ingresador por consola, creando una funcion para que el mismo se desarrolle correctamente.

# Importamos la funcion reduce, que se encuentra en el modulo functools.
from functools import reduce                     

      
# Creamos dos variables de tipo int, las cuales almacenaran el numero ingresado por consola. Y retorna al usuario el texto que le delegamos.

num1 = int(input("Ingrese un numero: "))               
num2 = int(input("Ingrese otro numero: "))

# Invocamos a def para crear nuestra funcion "resta", y le pasamos dos parametros ("a" y "b").
def resta(a, b):
    return a - b    # En esta linea el return establece/devuelve el resultado de nuestra funcion. Le ordenamos que reste los dos parametros ingresados.

# Saldra por consola el contenido del print y el resultado de nuestra funcion. 
print("El resultado de la resta es:", resta(num1, num2))  # Tambien llamamos a la funcion y le pasamos los parametros ( le pasamos las dos variables que almacenan los numeros ingresados por el usuario).
 
 
# Incorporamos la funcion "reduce".

valores = (num1, num2)  # Creamos la variable para que almacene los dos numeros ingresados por consola.

resta1 = reduce(resta, valores)  # Linea reducida para ejecutar la funcion. A la fn le pasamos la funcion(calculo) y la coleccion de valores.

print(f"Resultado uilizando la fn: {resta1}")  # Imprimimos por consola el texto y llamamos a nuestra funcion que devolvera solo el resultado.