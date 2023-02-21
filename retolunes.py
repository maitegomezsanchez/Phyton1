import random
min=5
max=100
#definición rangos
#n =range(5,10)
#ad=range(11,22)
#j=range(23,40)
#med=range(41,65)
#mayor=range(66,100)
#i=random.randint(min,max)
rangoedad=["niño","adolescente","joven","mediana edad","mayor"]

for r in rangoedad:
        accion= input(f"Eres {r} (S,N)?")
        if accion.upper()=="S":
            break
if r=="niño":
    min=5
    max=10
elif r=="adolescente":
    min=11
    max=22
elif r=="joven":
    min=23
    max=40
elif r=="mediana edad":
    min=41
    max=65
else: 
    min=66
    max=100
z=random.randint(min,max)
accion= input(f"Tu edad es  {z} (S,N)?")
while accion.upper()=="N":
    aux= input(f"Tu edad es > que {z}  (S,N)?")
    if aux.upper()=="S":
        min=z
    else:
        max=z
    z=random.randint(min,max)
    accion= input(f"Tu edad es  {z} (S,N)?")
print(f"Tu edad es {z}")



    
