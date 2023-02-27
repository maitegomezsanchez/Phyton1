def calcular_cuenta(total,propina=0.10):
    total = total + (total*propina)
    return total
def calculartotal(*arguments):
    totalsum=0
    print(f"numero de argumentos {len(arguments)}")
    for number in arguments:
        totalsum += number
    print(totalsum)

def imprimir_diassemana(*dias):
    #dias no se le puede añadir un contador pq no es nº. es necesario variable
    cont=1
    for d in dias:
        print(f"{d} es el {cont} de la semana")
        cont +=1
#for i in range(len(dias)) otra opcion

def ref_demo(x):
    x=42
    print(x)
def incrementar_ciudad(cities):
    cities.append("Madrid")

x=100
ref_demo(x)
print(x)
if __name__=="__main__":
    # #calcular factura con 10% propina
    # factura=calcular_cuenta(100)
    # print(f"Total de la cuenta es € {factura}")
    #    #calcular factura con 12% propina
    # factura=calcular_cuenta(100,0.12)
    # print(f"Total de la cuenta es € {factura}")
    x=100
    ref_demo(x)
    print(x)
    ciudades = ["Donosti", "Bilbo"]
    incrementar_ciudad(ciudades)
    print(ciudades)
    calculartotal(5,4,3,2,1,10,20)
    imprimir_diassemana("lunes","martes","miercoles","jueves","viernes")
    print("-"*20)
    imprimir_diassemana("lunes","martes","miercoles","jueves","viernes","sabado","domingo")

