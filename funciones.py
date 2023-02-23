def suma(n1,n2):
    return(n1+n2)
def resta(n1,n2):
    return(n1-n2)

def imprimir(lenguajeprog):
    print(f"{lenguajeprog} es un lenguaje de programacion")

if __name__=='__main__':
    num1=float(input("inserta 1nº para realizar suma"))
    num2=float(input("inserta 2nº para realizar suma"))
    if suma(num1,num2)>10:
        print(f"{suma(num1,num2)} es mayor q 10")
    else: 
        print(f"{suma(num1,num2)} es menor o igual a 10")
