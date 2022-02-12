
def ValidadateDia(dia):
    if dia>= 1 and dia <=31:
        return True
    else:
        return False

def ValidadateMes(mes):
    if mes >= 1 and mes <= 12:
        return True
    else:
        return False

def ValidadateAnio(anio):
    if anio >= 1 and mes <= 2022:
        return True
    else: 
        return False
        


def centrar(cad):

	print(" " * int(40 - (len(cad)/2)), cad)
	print(" " * int(40 - (len(cad)/2)), "=" * len(cad))


mensaje1 = "HackWomen"
centrar(mensaje1)
mensaje2 = "SKILLS FOR WOMEN IN TECH"
centrar(mensaje2)


print("INGRESE LA FECHA")
dia= int(input("dia:"))
mes= int(input("mes:"))
anio= int(input("anio:"))
print("el dia que eligio es:",ValidadateDia(dia),"el mes que eligio fue:",ValidadateMes(mes),"el año que eligio fue",ValidadateAnio(anio))

