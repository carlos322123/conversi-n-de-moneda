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


def conversor_soles():

    print()
    print("1) Dólares. \n"
          "2) Euros. \n"
          "3) Yens.")
    print()
    opcionS = str(input("Elija la moneda a la que desee convertir: "))

    if opcionS == "1":
       conversor_soles_dolares()
       menu()
    if opcionS == "2":
        conversor_soles_euros()
        menu()
    if opcionS == "3":
        conversor_soles_yens()
        menu()
    else:
        print("No existe la opción seleccionada.")
        print("Inténtelo de nuevo.")
        conversor_soles()

def conversor_soles_dolares():
    print()
    sd = float(input("introduzca el monto a cambiar: "))
    sd_final = sd * 0.27
    print("el monto es: ",sd_final)

def conversor_soles_euros():
    print()
    se = float(input("introduzca el monto a cambiar: "))
    se_final = se * 0.25
    print("el monto es: ",se_final)

def conversor_soles_yens():
    print()
    sy = float(input("introduzca el monto a cambiar: "))
    sy_final = sy * 34.24
    print("el monto es: ",sy_final)



def conversor_dolares():

    print()
    print("1) soles. \n"
          "2) Euros. \n"
          "3) Yens.")
    print()
    opcionS = str(input("Elija la moneda a la que desee convertir: "))

    if opcionS == "1":
       conversor_dolares_soles()
       menu()
    if opcionS == "2":
        conversor_dolares_euros()
        menu()
    if opcionS == "3":
        conversor_dolares_yens()
        menu()

    else:
        print("No existe la opción seleccionada.")
        print("Inténtelo de nuevo.")
        conversor_dolares()

def conversor_dolares_soles():
    print()
    ds =float(input("introduzca el monto a cambiar: "))
    ds_final = ds * 3.73
    print("el monto: ",ds_final)
def conversor_dolares_euros():
    print()
    de =float(input("introduzca el monto a cambiar: "))
    de_final = de * 0.94
    print("el monto: ",de_final)
def conversor_dolares_yens():
    print()
    dy =float(input("introduzca el monto a cambiar: "))
    dy_final = dy * 127.75
    print("el monto: ",dy_final)




def conversor_euros():

    print()
    print("1) soles. \n"
          "2) dolares. \n"
          "3) Yens.")
    print()
    opcionS = str(input("Elija la moneda a la que desee convertir: "))

    if opcionS == "1":
       conversor_dolares_soles()
       menu()
    if opcionS == "2":
        conversor_dolares_euros()
        menu()
    if opcionS == "3":
        conversor_dolares_yens()
        menu()

    else:
        print("No existe la opción seleccionada.")
        print("Inténtelo de nuevo.")
        conversor_euros()

def conversor_euros_soles():
    print()
    es = float(input("introduzca el monto a cambiar: "))
    es_final = es * 3.98
    print("el monto es: ",es_final)
def conversor_euros_dolares():
    print()
    ed = float(input("introduzca el monto a cambiar: "))
    ed_final = ed * 1.07
    print("el monto es: ",ed_final)
def conversor_euros_yens():
    print()
    ey = float(input("introduzca el monto a cambiar: "))
    ey_final = ey * 136.57
    print("el monto es: ",ey_final)


def conversor_yens():
    
    print()
    print("1) soles. \n"
          "2) euros. \n"
          "3) dolares.")
    print()
    opcionS = str(input("Elija la moneda a la que desee convertir: "))

    if opcionS == "1":
       conversor_yens_soles()
       menu()
    if opcionS == "2":
        conversor_yens_euros()
        menu()
    if opcionS == "3":
        conversor_yens_dolares()
        menu()

    else:
        print("No existe la opción seleccionada.")
        print("Inténtelo de nuevo.")
        conversor_yens()

def conversor_yens_soles():
    print()
    ys = float(input("ingrese el monto a cambiar: "))
    ys_final = ys * 0.029
    print("el monto es: ",ys_final)
def conversor_yens_euros():
    print()
    ye = float(input("ingrese el monto a cambiar: "))
    ye_final = ye * 0.0073
    print("el monto es: ",ye_final)
def conversor_yens_dolares():
    print()
    yd = float(input("ingrese el monto a cambiar: "))
    yd_final = yd * 0.0078
    print("el monto es: ",yd_final)




print("Bienvenido")
print()
menu()