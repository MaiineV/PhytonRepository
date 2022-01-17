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
