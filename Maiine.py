# region Uso basico de las clases y variables
def print_hi(name, age):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}. Your age is {age}')  # Press Ctrl+F8 to toggle the breakpoint.


userName = 'Ino'
userAge = 21
# Press the green button in the gutter to run the script.
if userName == 'Maine':
    print_hi(userName, userAge)

userName = 'Christian'
userAge = 20
print_hi(userName, userAge)
# endregion

# region Clases con estructuras y variables internas de la clase


class NewComputer:
    def __init__(self, cpu='Intel', gpu='Nvidia', ram='Hyperx'):
        print('My Computer is Building')
        self.cpuPart = cpu
        self.gpuPart = gpu
        self.ramPart = ram

    def showpcpart(self):
        print(f'My cpu is a {self.cpuPart}, my gpu is a {self.gpuPart} and my ram is a {self.ramPart}')


maiinePC = NewComputer('I7', 'GTX1660', '16GB')
maiinePC.showpcpart()

titianPC = NewComputer('I9', 'GTX1060', '32BG')
titianPC.ssdPart = '240GB'
titianPC.showpcpart()
print(f'And he bought a new disc, the total space is {titianPC.ssdPart}')
print('But after that, his gpu has broken')
del titianPC.ssdPart
titianPC.gpuPart = '3060TI'
titianPC.showpcpart()
# endregion

# region Arrays y List. Funciones del mismo
age = [1, 7, 14]
print(age)

age += [34, 140, 370]  # Se puede usar con todas las operaciones matematicas, sea multiplicar, sumar, restar o dividir
print(age)

age.remove(34)  # Remueve uno basado en su valor
print(age)

age.pop(4)  # Remueve uno basado en su index
print(age)

del age[1]  # Remueve tmb uno basado en su index
print(age)

age.append('Hola')  # Suma al array el valor que le pases, Los arrays pueden ser de distintas variables, no solo de una
print(age)

ageLength = len(age)  # Conseguir el length de un array
print(ageLength)

print(age[: 2])  # Puedo elegir que parte del array usar

multiAge = [[15, 18, 32], [7, 5, 4], [3], [14, 132]]  # Podes hacer arrays de varias matrices
print(multiAge)
print(multiAge[1])
print(multiAge[2])
print(multiAge[0][2])
print(multiAge[3][0])

print(type(userName))  # Print del tipo de variable
# endregion

# region Multiples Variables y funciones para str
name, age, cute = 'Maiine', 21, False # Multiples variables
print((name, age, cute))

print(len(name))  # Print longitud de la palabra o lo que le pidas
print(name.find('i'))  # Devuelve el index de la primera letra coincidente
print(name.capitalize())  # Mayuscula a la primera letra
print(name.upper())  # Pone en mayuscula la palabra
print(name.lower())  # Pone en minusculas
print(name.isdigit())  # Revisa si son digitos numericos, devuelve booleanos
print(name.isalpha())  # Revisa si son letras, devuelve booleanos
print(name.count('i'))  # Cuenta la cantidad de 'i' que hay
print(name.replace('i', 'e'))  # Reemplaza la variable que le pidas, por la que le des
print(name*3)  # Multiplica el valor que le pases, sirve con str
# endregion

# region Account Creation
# Creacion de cuenta con Input en consola y While
'''
account_Create = False

while not account_Create:
    new_UserName = input('Select your username ')
    new_PassWord = input('Select your password ')
    new_PassWord_Confirm = input('Confirm your password ')
    # Los Inputs son strings, hay que transformarlos si querermos otro valor

    if new_PassWord == new_PassWord_Confirm:
        print('Your account was succesfully create')
        account_Create = True
    else:
        print('The passwords is not the same')
'''
# endregion

# region Imports y math
# Podes importar lo que sea sin rerferencia que genial es esto la concha de la lora
import ImportGeneral
ImportGeneral.print_this('Re Loco el Import')

import math
# Usando math. podes ver todas las funciones disponibles

pi = 3.14
x = 1
y = 2
z = 3

print(round(pi))  # Redondea el valor que le pases
print(math.ceil(pi))  # Redondea hacia arriba
print(math.floor(pi))  # Redondea hacia abajo
print(abs(pi))  # Hace el modulo de un valor, osea su valor absoluto
print(pow(pi, 2))  # Hace potencia de la base, y luego se escribe el exponente
print(math.sqrt(pi))  # Raiz del numero
print(max(x, y, z))
print(min(x, y, z))
# endregion

# region Strings Slice
userName = 'Maiine'
print(userName[0:3])  # Los string tmb funcionan como arrays y podes pedir segun el index
print(userName[0::2])  # El ultimo valor es los caractere que salta, 1 es el valor basico, con 2, omite una letra cada 2
print(userName[slice(2, 5)])  # Parte el texto segun el index pasado
# endregion

# region Logical Operator
booleano1 = True
booleano2 = False
booleano3 = True

if booleano1 == booleano2 and booleano2 == booleano3:
    print('Son todos iguales')
elif booleano1 == booleano2 or booleano1 == booleano3:
    print('Algunos son iguales')
elif not booleano1:
    print('Booleano 1 es falso')
# endregion
