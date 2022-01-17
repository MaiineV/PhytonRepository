"""Variable = a container for a value. Behaves as the value that it contains,
basicamente es un contenedor para un valor, puede ser para valores, numeros, y
"boleeans" lo cuales pueden ser -true or false- """

""" Al printear variables ejemplo: name = "helado" colocar comillas  y  print(name)  no usar comillas en el name """

name = "christian"
print(name)

"""String o str = a series of characters, una cadena de caracteres"""

print("hola " +name)
print(type(name))

""" se pueden combinar las variables en una multiple siempre y cuando sean del mismo tipo, con la palabra "type" se puede saber que tipo de variable es
como en el ejemplo de arriba."""

primer_nombre = "Christian"
segundo_nombre = "Natel"
nombre_completo= primer_nombre + segundo_nombre

print("hola"+nombre_completo)