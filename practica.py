

def centrar(cad):

    print(" " * int(40 - (len(cad)/2)), cad)
    print(" " * int(40 - (len(cad)/2)), "=" * len(cad))


mensaje1 = "HackWomen"
centrar(mensaje1)
mensaje2 = "SKILLS FOR WOMEN IN TECH"
centrar(mensaje2)


lista=[]
print("Bienvenidas")
print("Elige una opcion:")
while True:
    print("1. Registrar")
    print("2. Consultar")
    print("3. Salir")
    opcion =int(input("elige una:"))
    if opcion==1:
            print("por favor registrate")
            mi_lista ={}
            mi_lista['nombre'] = str(input("introduce tu nombre:"))
            mi_lista['edad'] = int(input("introduce tu edad:"))
            mi_lista['tema'] = input("introduce tu tema:")
            lista.append(mi_lista)
          
            if mi_lista['edad'] >= 18:
                print("es mayor pasale :)")
                
            else:
                 print("es menor lo siento :(")
                
           
    elif opcion==2:  
            #veces=int(input("¿cuantos registros quiere?"))
            for mi_lista in lista:
                    print(mi_lista)
            for key in mi_lista:
                print(f"{key}: {mi_lista[key]}",)
    
    elif opcion==3:
        break
    else:
        print("no es opcion correcta")

