# region Imports Utiles
import time  # Libreria de time
import math  # Libreria de funciones matematicas
import os  # Libreria de sistema operativo
import shutil  # Libreria para el copiado de archivo
# endregion

# region Finished Classes
"""
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

booleano1 = None  # Este es el Null, para declarar una variable vacia
booleano1 = 4
print(booleano1)  # Si lo declaras como None, la variable pasa a ser generica y podes volver a setearla
# endregion

# region For and Basic Time
bool_region_for = False
for_lenght = 10
for_top_lenght = 50
for_name = 'Maiine'

if bool_region_for:
    # For Basico
    for i in range(for_lenght):
        print(i)

    # For con punto de inicio y de final
    for i in range(for_lenght, for_top_lenght):
        print(i)

    # For con punto de inicio, final y step para saber cada cuanto print, aca se realiza cada 2
    for i in range(for_lenght, for_top_lenght, 2):
        print(i)

    # Podes hacer un for en el rango de un string o un array
    for i in for_name:
        print(i)

    for i in range(for_lenght, 0, -1):
        print(i)
        time.sleep(1)  # Como esperar tiempo y usar los time
# endregion

# region Loop Statement Controllers

while True:
    name = input('Whats your name? ')
    if name != '':
        break

phone_number = '15-3894-3036'

for i in phone_number:
    if i == '-':
        continue
    print(i, end='')  # El end hace cambiar el final del print, todo print termina con enter, aca se cambia a espacio

for i in range(1, 21):
    if i == 13:
        pass  # Pass no hace nada, solo un placeholder
    else:
        print(i)

# endregion

# region Tuple
# Basicamente es una lista pero ordena y no se puede modificar
programmer = ('Maiine', 21, 'male')

print(programmer.count("Maiine"))  # Devuelve la cantidad de veces que aparece la variable
print(programmer.index(21))  # Devuelve el index de la variable

# Podes crear un if junto con un for para que revise una lista o un tuple
if 'Maiine' in programmer:
    print('Maiine is here')
# endregion

# region Set
# Set es una lista, mas rapida y de menos recursos, que no tiene orden ni index y
# no admite valores duplicados, no los cuenta

utensils = {'fork', 'spoon', 'knife'}
dishes = {'bowl', 'plate', 'cup', 'fork'}

# utensils.update(dishes)  # Con update anadis a la primera lista lo de las segunda
# dinner_table = utensils.union(dishes)

# utensils.add('CookingKnife')
# utensils.remove('fork')
# utensils.clear()  # Limpia listas o arrays

# for i in dinner_table:
#    print(i)

# print(utensils.difference(dishes))  # Diferencias entre ambas listas, devuelve los valores de la primera
# print(utensils.intersection(dishes))  # Devuelve lo que sea igual en amabas
# endregion


# region Diccionarios

capitals = {'USA': 'Washington',
            'India': 'New Dehli',
            'China': 'Beijin',
            'Rusia': 'Moskow'}

# Con update se puede anadir nuevos o modficiar viejos si usan la misma key
capitals.update({'Argentina': 'CABA'})
capitals.update({'USA': 'Las Vegas'})

# Pop borra los datos, para evita errores primero se chequea con get
city_to_delete = 'Maxico'
if capitals.get(city_to_delete) is not None:
    capitals.pop(city_to_delete)
else:
    print('Esa ciudad no se encuentra en la lista')

# Funciones para diccionarios
print(capitals.get('Argentina'))
print(capitals.values())
print(capitals.keys())
print(capitals.items())

# For en diccionarios
for key, value in capitals.items():
    print(key, value)
# endregion

# region Keyword Arguments


def hello(name, age, sex):
    print('Your name is ' + name)
    print('Your age is ' + str(age))
    print('Your sex is ' + sex)


# Se puede seleccion a que condicion asignarle cada valor
hello(age=21, name='Maiine', sex='male')
# endregion


# region Arguments


def plus(*args):
    num = 0
    args = list(args)  # Para crea una lista con las variables que se pasan
    for i in args:
        num += i
    return num


print(plus(48, 16, 39, 62, 87, 0))
# endregion

# region Kwargs
# Los kwargs son argumentos pero odenados en un diccionario, asi pudiendo pasarlos con keywords para su orden
# Va en orden segun se anaden


def hello(**kwargs):
    print('Hi ' + kwargs['name'] + '! Im waiting for you for like ' + kwargs['time_waiting'])


hello(name='Maiine', time_waiting='2 hours')
# endregion


# region String Format

animal = 'Cow'
item = 'Table'

# Se puede dejar sin definir, definiendo por valor de index o por keyword
text = 'The {} jump over the {}'
text = 'The {0} jump over the {1}'
text = f'The {animal} jump over the {item}'

print(text.format(animal, item))

# Manera de ordenar los textos para los outputs
name = 'Maiine'

print('Hi {:10}'.format(name))
print('Hi {:>10}'.format(name))
print('Hi {:<10}'.format(name))
print('Hi {:^10}'.format(name))

# Manera de cambiar la notacion de los numeros
number = 10003.141968

print('The number is {:.3f}'.format(number))  # Selecciona cuantos decimales muestra
print('The number is {:,}'.format(number))  # Si anade comas cada 3 digitos
print('The number is {:E}'.format(number))  # Mostrar con notacion cientifica
# endregion

# region Random
import random

x = random.randint(1, 6)  # Inclusive con el primer y ultimo valor a diferencia de C#
y = random.random()  # Esto devuelve un float entre 0 y 1

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)  # Esto elige un valor aleatorio dentro de la lista

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'J', 'Q', 'K', 'A']
random.shuffle(cards)  # Esto mezcla la lista que le pasemos

# endregion

# region Exception

try:  # Intenta lo que tenga dentro, si sale bien, sigue, sino entra en un except
    numerator = int(input('Select a numerator: '))
    denominator = int(input('Select a denominator: '))
    result = numerator / denominator
except ZeroDivisionError as e:  # El nombre al lado de except declara que error especifico trata (No dividir por 0)
    print('You cant divide by 0')
    print(e)  # 'as e' sive para denominar un nombre al error que ocurre, print hace que muestre que error es en consola
except ValueError as e:  # Este error se basa en si es otro tipo de variable
    print('Only numbers please')
    print(e)
except Exception as e:  # Esto cubre todos los except que no se declaren antes, siempre deberia ir ultimo
    print('Something went wrong')
    print(e)
else:  # Si el try funciona bien y no se activa ningun except, pasa al else
    print(result)
finally:  # Haya un error o no, finally siempre se ejecuta al final de la cadena
    print('The end')

# endregion



# region File Detection
path = 'C:\\Users\\agust\\Documents\\GitHub\\PhytonRepository\\PyTest.txt'
# Al final de cada archivo hay que agregarle la terminacion del mismo

if os.path.exists(path):  # Revisa si la ruta existe
    print('The path exist')
    if os.path.isfile(path):  # Revisa si es un archivo
        print('Is a file')
    elif os.path.isdir(path):  # Revisa si es una carpeta
        print('Is a directory')
else:
    print('The path dont exist')
# endregion

# region Read a File

# Esto abre el archivo, si se encuentra en el proyecto, solo es necesario el nombre
# Sino, hay que ponerle el path entero como arriba
try:  # Si no encuentra el archivo, va a tener un error, usando un try y un except lo solucionamos
    with open('PyTest.tx') as file:
        print(file.read())
        print(file.closed)  # Devuelve si el archivo esta cerrado, dentro del with abierto, se cierra cuando sale
except FileNotFoundError as e:
    print('I cant find the file')

# endregion

# region Write a File

text = '\nBueno, deberia andar'

# with open('PyTest.txt', 'w') as file:  # Modulo 'w' es para reescibir un documento
#    file.write(text)

with open('PyTest.txt', 'a') as file:  # Modulo 'a' es para sumar el texto al ya escrito
    file.write(text)
# endregion

# region Copy a File
'''
# Necesita import de shutil
# copyfile() = copia el contenido de un archivo
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (Creacion del archivo y las modificaciones) 
'''

shutil.copyfile('PyTest.txt', 'D:\\Desktop\\Copy.txt')  # Hay que poner una fuente y a donde va
# endregion

# region Move File

source = 'D:\\Desktop\\Copy.txt'
destination = 'D:\\Desktop\\Pruebaxd\\Copy.txt'

try:
    if os.path.exists(destination):
        print('There is already a file here')
    else:
        os.replace(source, destination)  # No se puede mover un archivo entre discos
        print('The file was move')
except FileNotFoundError:
    print('No encontre el archivo')
# endregion

# region Delete File

the_file = 'NewFolder'

# os.remove(the_file)  # Esto sirve para borrar un archivo, pero no un directorio
# os.rmdir(the_file)  # Esto sirve para borrar un directorio, solo si esta vacio
# shutil.rmtree(the_file)  # Esto sirve para borrar un directorio con cosas dentro
# endregion

# region Modular

# import ImportGeneral
# import ImportGeneral as Imp
from ImportGeneral import print_this as pr, hi  # Esto puede importar mas de un def
# Diferentes tipos de imports
pr('Hiiii')
hi()

help('modules')  # Esto te muestra todos los modulos disponibles

"""
# endregion

# region Class, Constructores y Class Variable
from ImportGeneral import Car

car_1 = Car('Nissan', '2021', 'Red')
car_2 = Car('Chevrolet', '2019', 'White')

print(car_1.model, car_1.year, car_1.color)
print(car_2.model, car_2.year, car_2.color)

car_1.drive()
car_2.stop()
# endregion

# region Herencias

class Animal:
    alive = True

    def sleep(self):
        print('Sleeping')

    def eat(self):
        print('Eating')

# Para la herencia luego de una clase, hay que poner entre () la clase padre
class Fish(Animal):
    pass

class Dog(Animal):
    pass

class Hawk(Animal):
    pass

# Para crear un objeto, hay que asignarle una clase a una variable
fish = Fish
dog = Dog
hawk = Hawk
