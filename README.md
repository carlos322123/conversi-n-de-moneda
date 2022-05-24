# conversi-n-de-moneda
primero definimos menú
def menu():
    print()
    print("1)   Soles. \n"
          "2)   Dólares. \n"
          "3)   Euros. \n"
          "4)   yens. \n")

    moneda = input("Ingrese la moneda a convertir: ")

    if moneda == "1":
        print()
        conversor_soles()

    if moneda == "2":
        print()
        conversor_dolares()
    if moneda == "3":
        print()
        conversor_euros()
    if moneda == "4":
        print()
        conversor_yens()
        
        definimos las variables de cada moneda para luego hacer el tipo de cambio con la moneda a la que se desea convertir
        
        definimos conversor_soles 
        def conversor_soles():

    print()
    print("1) Dólares. \n"
          "2) Euros. \n"
          "3) Yens.")
    print()
    opcionS = str(input("Elija la moneda a la que desee convertir: "))

y luego definimos a que valor se desea convertir y así con las demás monedas para poder hacer la conversión con las demás monedas entre si.
