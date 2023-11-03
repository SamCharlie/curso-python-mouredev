#EXCEPTIONS HANDLING (manejo de errores)

numberOne, numberTwo = 5, 1

#numberTwo = "1"

try:
    print(numberOne + numberTwo)
    print("No se a producido error")
except:
    #Se ejecuta si se produce un error
    print("Se a producido un error")
else: #opcional
    #Se ejecuta si no se produce un error
    print("La ejecucion continua")
finally: #opcional
    #Se ejecuta siempre alla o no error
    print("la ejecucion continua otra vez")

print("Carlitos feliz")

#Captura de excepciones por tipo

try:
    print(numberOne + numberTwo)
    print("No se a producido error")
except ValueError:
    #Se ejecuta si se produce un error
    print("Se a producido un VauleError!")
except TypeError:
    #Se ejecuta si se produce un error
    print("Se a producido un TypeError!")

# Captura de la informacion de la excepcion

try:
    print(numberOne + numberTwo)
    print("No se a producido error")
except ValueError as error:
    #Se ejecuta si se produce un error
    print(error)
except Exception as exceptionerror:
    #Se ejecuta si se produce un error
    print(exceptionerror)

print("Carlitos feliz")