# Uso basico de las clases y variables
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


# Clases con estructuras y variables internas de la clase
class NewComputer:
    def __init__(self, cpu='Intel', gpu='Nvidia', ram='Hyperx'):
        print('My Computer is Building')
        self.cpuPart = cpu
        self.gpuPart = gpu
        self.ramPart = ram

    def showPCPart(self):
        print(f'My cpu is a {self.cpuPart}, my gpu is a {self.gpuPart} and my ram is a {self.ramPart}')


maiinePC = NewComputer('I7', 'GTX1660', '16GB')
maiinePC.showPCPart()

titianPC = NewComputer('I9', 'GTX1060', '32BG')
titianPC.ssdPart = '240GB'
titianPC.showPCPart()
print(f'And he bought a new disc, the total space is {titianPC.ssdPart}')
print('But after that, his gpu has broken')
del titianPC.ssdPart
titianPC.gpuPart = '3060TI'
titianPC.showPCPart()


# Arrays y List. Funciones del mismo
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

print(type(userName)) # Print del tipo de variable

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

