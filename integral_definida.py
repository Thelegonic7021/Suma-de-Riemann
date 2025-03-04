import math

def pi(valor):
    if valor.lower() == 'pi':
        return math.pi
    else:
        return float(valor)

def main():
    sumatoria = 0
    fi = []
    #Ingresar datos de intervalos
    int_superior = pi(input("Ingrese el límite superior de la integral: "))
    int_inferior = pi(input("Ingrese el límite inferior de la integral: "))

    #Si digita un numero mayor en el extremo inferio al del mayor cancelara el calculo
    if int_inferior >= int_superior:
        print("El intervalo inferior se registro que es mayor al superior\n ERROR 404")
        return 0

    #Valor de numero de particiones del intervalo
    n = int(input("Ingrese el valor de n"))

    fx = input("Ingrese la funcion a integrar: ")

    delta = (int_superior-int_inferior)/n

    print(f"△x = {delta}")
    i=0

    # Guarda en una lista cada valor probado de x en la función para hacer la sumatoria
    for i in range(n):
        x = (i+1)*delta
        fx_eval = fx.replace("x",str(x)).replace("sin","math.sin").replace("cos","math.cos").replace("tan","math.tan")
        fi.append(eval(fx_eval))
    print(fi)

    #Realiza la sumatoria de los valores guardados en la lista
    
    for i in range(n):
        sumatoria += fi[i]*delta
    print(f"Sumatoria = {sumatoria}")

if __name__ == "__main__":
    main()
