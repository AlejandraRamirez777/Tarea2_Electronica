import numpy as np
import matplotlib.pyplot as plt

#Im1 en funcion de Vin
def Im1(Vin):
    a = (1/15.0)*(Vin+10.7)
    b = (1/30.0)*(-6.4)
    ans = a+b
    return ans

#Im2 en funcion de Vin
def Im2(Vin):
    a = (1/30.0)*(Vin+10.7)
    b = (1/15.0)*(-6.4)
    ans = a+b
    return ans

#Valores de Vin
VVin = np.linspace(-20,20,100)

#Im1 y Im2 evaluados
IIm1 = Im1(VVin)
IIm2 = Im2(VVin)

#Linea de I = 0
zero = np.zeros(100)

#Corrientes de Diodos
Id1 = IIm2 - IIm1
Id2 = IIm2

#Graficas
#plt.plot(VVin,IIm1, label = "Im1")
plt.plot(VVin,Id1, c = "g", label = "Id1")
plt.plot(VVin,IIm2, c = "r", label = "Id2")
plt.plot(VVin, zero, c = "k")
plt.legend(loc = 2)
plt.title("Id1 y Id2 vs Vin")
plt.xlabel("Voltaje en (Vin) [V]")
plt.ylabel("Corriente [mA]")
plt.savefig("Id1_Id2__Vin.png")
plt.clf()

#Constantes
Vc1 = -10.7
Vc2 = 5.7
R1 = 10000.0
R2 = R1
R3 = R1
V1 = 10.0
V2 = 5.0
Vg = 0.7

#Funcion de Vo
def Vo(Vin):
    ans = np.array([])
    for i in Vin:
        if  i < Vc1:
            a = ((R2/(R2+R1))*i) - Vg - V2
            ans = np.append(ans,a)
        elif  Vc1 < i < Vc2:
            ans = np.append(ans,i)
        else:
            b = ((R3/(R3+R1))*i) + Vg + V2
            ans = np.append(ans,b)
    return ans

#Linea de Vc1
one = np.ones(100)
vcc1 = one*Vc1
#Linea de Vc2
vcc2 = one*Vc2

#Grafica
plt.plot(VVin,Vo(VVin),c ="k")
plt.plot(vcc1,VVin, c = "c", label = "Vc1")
plt.plot(vcc2,VVin, c = "y", label = "Vc2")
plt.legend(loc = 2)
plt.title("Vo vs Vin")
plt.xlabel("Voltaje en Vin [V]")
plt.ylabel("Voltaje en Vo [V]")
plt.savefig("Vo_vs_Vin.png")
plt.clf()


#Regiones D1 y D2

Vv1 = np.ones(100)*V1
Vv2 = np.ones(100)*V2

#Voltaje Diodo1
Vd1 = -Vv1  - VVin
#Voltaje Diodo2
Vd2 = VVin - Vv2

#Linea de Vg = 0.7
Vvg = np.ones(100)*Vg

#Graficas
plt.plot(VVin,Vd1, c = "y", label = "Vd1")
plt.plot(VVin,Vd2, c = "r", label = "Vd2")
plt.plot(VVin, Vvg, c = "g")
plt.plot(VVin, zero, c = "k")
plt.legend(loc = 2)
plt.title("Voltaje diodos vs Vin")
plt.xlabel("Voltaje en Vin [V]")
plt.ylabel("Voltaje en diodos [V]")
plt.savefig("VD_vs_Vin.png")
