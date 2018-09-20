import numpy as np
import matplotlib.pyplot as plt

#Im1 en funcion de Vin
def Im1(Vin):
    a = (1/15.0)*(Vin+9.3)
    b = (1/30.0)*(-13.6)
    ans = a+b
    return ans

#Im2 en funcion de Vin
def Im2(Vin):
    a = (1/30.0)*(Vin+9.3)
    b = (1/15.0)*(-13.6)
    ans = a+b
    return ans

#Valores de Vin
VVin = np.linspace(-20,20,100)

#Im1 y Im2 evaluados
IIm1 = Im1(VVin)
IIm2 = Im2(VVin)

#Linea de I = 0
zero = np.zeros(100)

A=0
for i in IIm1:
    if i<0.01 and i>-0.01:
        print "Vm1 = " + str(VVin[A])
    A+=1

B=0
for i in IIm2:
    if i<0.01 and i>-0.01:
        print "Vm2 = " + str(VVin[B])
    B+=1

Id1 = IIm2 - IIm1

C=0
for i in Id1:
    if i<0.01 and i>-0.01:
        print "Vd1 = " + str(VVin[B])
    C+=1

#Graficas
plt.plot(VVin,IIm1, label = "Im1")
plt.plot(VVin,IIm2, c = "r", label = "Im2")
plt.plot(VVin,Id1, c = "g", label = "Id1")
plt.plot(VVin, zero, c = "k")
plt.legend(loc = 2)
plt.title("Im1 y Im2 vs Vin")
plt.xlabel("Voltaje en (Vin) [V]")
plt.ylabel("Corriente [mA]")
plt.savefig("Im1_Im2__Vin.png")
plt.clf()

#Constantes
Vc1 = -1000.0
Vc2 = 17.9
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
        if i < Vc2:
            ans = np.append(ans,i)
        else:
            a = ((R3/(R3+R1))*i) - Vg + V2
            ans = np.append(ans,a)
    return ans

#Linea de Vc2
one = np.ones(100)
vcc2 = one*Vc2

#Grafica
plt.plot(VVin,Vo(VVin))
plt.plot(vcc2,VVin, c = "y", label = "Vc2")
plt.legend(loc = 2)
plt.title("Vo vs Vin")
plt.xlabel("Voltaje en Vin [V]")
plt.ylabel("Voltaje en Vo [V]")
plt.savefig("Vo_vs_Vin.png")
plt.clf()
