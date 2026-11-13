"""Crea la función con el nombre exacto que se solicita y 
recibe un único parámetro (numbers), que será una lista como [2, 5, 3].
return sum(numbers): Utiliza la función nativa sum() de Python para sumar todos 
los elementos de la lista y devuelve (return) el resultado final. 
Nota: Es obligatorio usar return y no print(), genera error para efectos de avaluarlo"""

def addmultiplenumbers(numbers):
    return sum(numbers)

"""result = 1: Se crea una variable acumulador, se inicia en 1 
(o el resultado siempre daría 0).
for num in numbers:: Recorre la lista número por número, uno tras otro.

result *= num: Multiplica el valor acumulado por el número actual de la lista 
(es equivalente a result = result * num).
return result: Una vez terminado el ciclo, devuelve el producto total."""

def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

"""num % 1 == 0: El operador módulo (%) obtiene el residuo de una división. 
Al dividir cualquier número entre 1, si el residuo es 0, 
significa que no tiene decimales  
Esto cumple el requisito de que sea un número entero (whole number).

and num % 2 == 0: Verifica al mismo tiempo que, al dividirlo entre 2, 
el residuo sea 0 (condicion para que sea par).

return True / return False: Si ambas condiciones se cumplen, 
devuelve el booleano True; de lo contrario, devuelve False."""

def isiteven(num):
    if num % 1 == 0 and num % 2 == 0:
        return True
    return False

"""if num % 1 == 0:: Al igual que en el paso anterior, 
comprueba si el número carece de parte decimal. 
Funciona tanto para enteros puros como para flotantes exactos, 
devolviendo True en ambos casos y False si tiene decimales."""

def isitaninteger(num):
    if num % 1 == 0:
        return True
    return False

"""def main():: Agrupa el código que se ejecutará cuando una persona abra el programa."""

def main():
    print("Hello learners!")
    
    print(addmultiplenumbers([2, 5, 3]))        # imprime 10
    print(multiplymultiplenumbers([2, 5, 3]))   # imprime 30
    print(isiteven(4))                          # imprime True
    print(isiteven(5))                          # imprime False
    print(isiteven(4.5))                        # imprime False
    print(isitaninteger(4.0))                   # imprime True
    print(isitaninteger(4.5))                   # imprime False

"""if __name__ == "__main__":: Esta condición verifica cómo se está ejecutando el archivo."""

if __name__ == "__main__":
    main()

