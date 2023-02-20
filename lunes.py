#while True:
#   print("hola")

""" i=0
while i<10:
   print("Hola" + str(i))
   i=i+1
else:
    print("else")

j=10
while j>0:
    if j==5:
        print("i es 5")
        break
    print("Hola" + str(j))
    j=j-1
print("fin bucle")
accion = input("quieres continuar (S,N?)")
while (accion=="S") or (accion=="s"):
    print("continua el bucle")
    accion = input("quieres continuar (S,N)?")
print("salida bucle") """
""" i=1
while i<10:
    print(i)
    i=i+1
total=0
while total<100:
    num=int(input("Introduce un número: "))
    total=total+num
print("El total es: ", total) """
""" i=100
while i>=50:
    print(f"i con valor {i} es mayor o igual que 50")
    i=i-1 """
i=0
while i<100:
    if i not in(10,20,30,40,50,60,70,80,90):
        print(i)
    i+=1
#otra forma de hacer lo mismo pero utilizando función range
i=0
while i in range(100):
    if i not in(10,20,30,40,50,60,70,80,90):
        print(i)
    i+=1