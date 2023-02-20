import random
min=5
max=100
#definición rangos
n =range(5,10)
ad=range(11,22)
j=range(23,40)
med=range(41,65)
mayor=range(66,100)
i=random.randint(min,max)
rangoedad=["niño","adolescente","joven","mediana edad","mayor"]

accion = input(f"Tu edad es {i} (S,N)?")
if accion.upper()=="N":
    for r in rangoedad:
        accion= input(f"Eres rangoedad[r] (S,N)?")
        if accion.upper()=="S":
            break
    


    
