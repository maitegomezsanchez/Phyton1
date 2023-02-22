
# nombres=["jon","maria","juan","asier"]
# nueva_lista=
# for nombre in nombres:
#     if nombre[0]=="j"
#         nueva_lista.append(nombre)

# #ejemplo list comprehension
# nombre es lo q se va añadir
# bucle y lo q devuelvo
# nombres=["jon","maria","juan","asier"]
# nl = [nombre for nombre in nombres if nombre[0] =="j"]
#otra forma
#nl = [nombre*2 for nombre in nombres]
#ejercicio
""" numeros =[3, 54, -12, 4, -67, 99, -120, 0]
lista_positiva = [n*2 for n in numeros if n>=0]
lista_negativa = [n for n in numeros if n<0]
print(lista_positiva)
print(lista_negativa) """

#hacer el ejercicio con un for de forma normal
# list_pos=[]
# list_neg=[]
# for i in numeros:
#     if i>=0:
#         list_pos.append(i)
#     else:
#         list_neg.append(i)
# print(list_pos)
# print(list_neg)

texto = "Pitón es un lenguaje de programación. Pitón está usado para la automación, análisis de datos e incluso la creación de páginas webs. Pitón fue creado por Bill Gates en 1960. Pitón es difícil de usar."
texto=texto.replace("Pitón", "Python")
print(texto)
texto = "    Lo más importante que nos ha mantenido en Python... bueno, hay 2 cosas importantes. Uno son las bibliotecas. La otra cosa que nos mantiene en Python, y esto es lo más importante, es facil de leer y entender. Cuando contratamos nuevos empleados. Solo digo, 'todo lo que escribas debe estar en python'. Sólo para que pueda leerlo. Y es increíble porque puedo ver desde el otro lado de la habitación, mirando su pantalla, si su código es bueno o malo. Porque un buen código de Python tiene una estructura muy obvia. Y eso hace que mi vida sea mucho más fácil        "
x= texto.swapcase()
print(x)
print(texto.upper())
if "código" in texto:
    print("código aparece en el texto")
else:
    print("código No aparece en el texto")
print('Number of occurrence of Python:', texto.count('Python'))
text_aux=texto.lower()
print('Number of occurrence of Python or python:', text_aux.count('python'))
print(id(texto))
y = texto.find("importante")
print(y)
y = texto.find("Python")
print(y)
#scojo un sunstring eliminando el primer Python - salto la P
aux=texto[y+1:len(texto)]
print(aux)
z = texto.strip()
print(z)
#COMO LO HA REALIZADO EL PROFE
texto=texto.upper().count("PYTHON")

#strip()
#lista=split()

nombreusuarios=[]
#lista de elementos
#emails = ["jon.smith@microsoft.com", "maria.fernandez@microsoft.com", "david@microsoft.com", "isabel@microsoft.es","alfonso@gmail.com"]
#for email in emails:
#     if nombre[0]=="j"
#         nombreusuarios.append(nombre)
#y = texto.find(".")
#print(y)
#scojo un sunstring eliminando el primer Python - salto la P
#aux=texto[y+1:len(texto)]
#devuelve una lista
texto="david@gmail.com"
a,b= texto.split("@")
#tipo es string pq va ""
print(type(a))
print(type(b))
print(a)
print(b)
lista_nombres=[]
lista_dominios=[]
emails = ["jon.smith@microsoft.com", "maria.fernandez@microsoft.com", "david@microsoft.com", "isabel@microsoft.es","alfonso@gmail.com"]
for email in emails:
    a,b= email.split("@")
    lista_nombres.append(a)
    if b not in lista_dominios:
        lista_dominios.append(b)
print(lista_nombres)
print(lista_dominios)
#segunda parte del ejercicio
nombres = ("maria", "jon", "david")
texto_CSV = [n+"@nazaret.eus" for n in nombres]
texto_CSV1 = ",".join(n+"@nazaret.eus" for n in nombres)
print(texto_CSV)
print(texto_CSV1)
