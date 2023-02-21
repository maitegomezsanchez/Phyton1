import random
y= random.randint(12,18)
if y==15:
    print("Es 15")
    print(f" es {y}")

nombres=["jon","maria","juan","asier"]
#tb funciona nombres=("jon","maria","juan","asier")
#genera valor aleatorio de la lista creada
y=random.choice(nombres)
if y=="juan" or y=="maria":
    print("juan y maria no están hoy en clase")
else: print("asier o jon si estan hoy en clase")