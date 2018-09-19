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
        print "Vc1 = " + str(VVin[A])
    A+=1

B=0
for i in IIm2:
    if i<0.01 and i>-0.01:
        print "Vc2 = " + str(VVin[B])
    B+=1

#Graficas
plt.plot(VVin,IIm1, label = "Im1")
plt.plot(VVin,IIm2, c = "r", label = "Im2")
plt.plot(VVin, zero, c = "k")
plt.legend(loc = 2)
plt.title("Im1 y Im2 vs Vin")
plt.xlabel("Voltaje in (Vin) [V]")
plt.ylabel("Corriente [mA]")
plt.savefig("Im1_Im2__Vin.png")
