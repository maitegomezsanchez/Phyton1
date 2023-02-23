import funciones
if __name__=='__main__':
    num1=float(input("inserta 1nº para realizar resta: "))
    num2=float(input("inserta 2nº para realizar resta: "))
    if funciones.resta(num1,num2)>10:
        print(f"la resta {resta(num1,num2)} es mayor q 10")
    else: 
        print(f"la resta {resta(num1,num2)} es menor o igual a 10")
