import funciones
import requests
if __name__=='__main__':
    num1=float(input("inserta 1nº para realizar resta: "))
    num2=float(input("inserta 2nº para realizar resta: "))
    if funciones.resta(num1,num2)>10:
       print(f"la resta {funciones.resta(num1,num2)} es mayor q 10")
    else: 
       print(f"la resta {funciones.resta(num1,num2)} es menor o igual a 10")
  
    link = "http://info.cern.ch/"
    r=requests.get(link)
    print(r.status_code) #si el resultado es 200 es pq ha encontrado la pagina
    html=r.text
    print(html)
    html=r.text.replace("Learn about CERN","just DO IT")
    print(html)