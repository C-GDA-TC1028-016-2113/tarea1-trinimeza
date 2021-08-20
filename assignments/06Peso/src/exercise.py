def main():
    #escribe tu código abajo de esta línea
    peso_inicial = float(input("Dame el peso inicial: "))
    peso_final = float(input("Dame el peso final: "))
    meses = float(input("Dame la cantidad de meses: "))
    peso_a_bajar = ((peso_inicial-peso_final)/meses)
    print("Lo que debes bajar por mes es:", peso_a_bajar)



if __name__ == '__main__':
    main()
