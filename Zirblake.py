# region variables
"""Variable = a container for a value. Behaves as the value that it contains,
basicamente es un contenedor para un valor, puede ser para valores, numeros, y
"boleeans" lo cuales pueden ser -true or false- """

""" Al printear variables ejemplo: name = "helado" colocar comillas  y  print(name)  no usar comillas en el name """

#name = "christian"
#print(name)

"""String o str = a series of characters, una cadena de caracteres"""

#print("hola "+name)
#print(type(name))

""" se pueden combinar las variables sueltas en una multiple siempre y cuando sean del mismo tipo, con la palabra "type"
 se puede saber que tipo de variable es
como en el ejemplo de arriba."""
# La siguiente combinacion de strings es de el tipo "data"
#first_name = "Christian"
#last_name = "Natel"
#full_name = first_name + " " + last_name

#print("hola " + full_name)

""" Int = integer, basicamente es un numero entero, sin comas"""
# Las int no van entre comillas, ya que si le agregas las comillas se convertiria en un string

#age = 20

#  shortcut ejemplo para hacer lo de arriba

#age = age + 1
#age += 1

# En este caso se sumaron 2 años por el shortcut mas la version normal

#print(age)
#print(type(age))
"""En el siguiente ejemplo no se permite el print debido a que  el texto es un -string- y estamos sumando un int, la
 forma de solucionarlo es convirtiendo el int en un string agrengadole la abreviacion -str- y el parentesis al int """
#print("tu edad es"+ age)
#solucion:

#print("tu edad es: " +str(age))

"""Variable float: floating point number ( un numero decimal ) basicamente en vez de ser un entero ahora es uno que 
puede almacenar una decima parte de un numero"""

#height = 250.5
#print(height)
#print("tu altura es: "+ str (height) + " centimetros")

"""Variable Stoolean, solo pueden contener un -True or False- """

#human = True
#print(human)
#print(type(human))
#print("sos un humano?: " + str(human))

#endregion
#region multiple assignment
"""el multiple asignamiento los que nos permite es asignar multiples variables al mismo tiempo en una misma
linea de codigo, basicamente utilizando las comas"""

#name, age, attractive = "Christian", 20, True

#print(name)
#print(age)
#print(attractive)

#Patricio = Esteban = Eduardo = Ignacio = 30

#print(Patricio)

#endregion
#region string methods
#name = "christian"
#print (len(name))
#la funcion "len" sirve para que te diga el largo de la variable
#print(name.find("t"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())
#print(name.count("r"))
#print(name.replace("r","h"))
#print(name*3)

#endregion
#region type casting
"""type casting es la capacidad de convertir una variable en otra variable"""

#x =  15
#y = 2.0
#z = "3"

#y = float(y)
#x = float(x)
#z = float(z)
#print(x)
#print(y)
#print(z*3)

#endregion
#region user input
"""input es cuando la consola te permite ingresar texto"""
#name = input("Cual es tu nombre?")
#age = int(input("Cual es tu edad?"))
#height = float(input ("Cuanto medis?"))

#print("Hola! " + name)
#print("Que grande sos! " + str(age) + " años")
#print("Medis unos " + str(height) + " centimetros")

#endregion
#region math functions
#import math

#pi = 3.14
#x = 1
#y = 2
#z = 3
#print(round(pi))
#print(math.ceil(pi))
#print(math.floor(pi))
#print(abs(pi))
#print(pow(pi,2))
#print(math.sqrt(pi))
#print(max(x,y,z))
#print(min(x,y,z))

#regionend
#region slicing
"""slicing sirve para crear un substring sacando datos de otro strings [start:stop:step]"""
#name = "Christian Natel"

#first_name = name[0:9]
#last_name = name[10:15]
#funky_name = name [0:15:3]
#reversed_name = name[::-1]
#Los corchetes, el primero es inclusivo y el ultimo es exclusivo
"""para abreviar puedo directamente poner :3 y me va a tomar el 0 como inicio y en el siguiente 10: y va a entender que
a partir de ese todos los de adelante"""
#print(first_name)
#print(last_name)
#print(funky_name)
#print(reversed_name)

#website1 = "http://google.com"
#website2 = "http://aslanstore.com"
#en el Slice se utiliza coma " , " no " : "
#slice = slice(7,-4)

#print(website1[slice])
#print(website2[slice])

#endregion
#region if statements
"""If statement: un bloque de codigo que va a ejecutar si(if) su condicion es verdadera(true)"""
#el orden del "if" "elif" o "else" importa, ya que el que este primero y se cumpla va a ser leido y los demas omitidos

#name = input("Cual es tu nombre?")
#age = int(input("Cual es tu edad?"))
#height = float(input("Cuanto medis?"))

#print("Hola! " + name)
#print("Tu altura es de: "+str(height))

#if age >= 18 :
    #print("Sos un adulto!")
#elif age < 0 :
    #print ("Aun no naciste!")
#else:
    #print("Sos un niño!")

#endregion
#region logical operators (and,or,not)
""" Son utilizados los logical operators (and, or, not) para checkear si dos o mas condicionales son true or false"""

#temp = int(input("Cual es la temperatura afuera?"))

#if temp >= 0 and temp <= 30 :
    #print("el clima esta lindo afuera!")
    #print("sali a dar un paseo!")
#elif temp < 0 or temp > 30 :
   # print ("el clima esta feo afuera!")
    #print ("no salgas!")

#para que el "and" sea valido y se proyecte ambas condiciones tienen que cumplirse, ejemplo si pongo -20 grados
#no se estaria cumpliendo el >= 0

#para utilizar el "not" hay que colocarle un parentesis a la condicional y agregarle el "not"
# ejemplo: if not(temp >= 0 and temp <= 30 ):           o        elif not(temp < 0 or temp > 30) :
#lo que hace el "not" es cambiar algo verdadero a falso o viceversa

#endregion
#region while loops
"""while loop es un statment que va a ejecutar su bloque de codigo mientra su condicion sea verdadera"""
#while 1==1 :
    #print("hola estoy atrapado en el loop aaaa")

#name = ""

#while len(name) == 0:
    #name = input("Cual es tu nombre?: ")

#print("Bienvenido! "+name)

"""otra forma de escribirlo"""

#name = None

#while not name :
    #name = input ("Cual es tu nombre?: ")

#endregion
#region for loops
