import numpy as np
import matplotlib.pyplot as plt

#Constantes
R1 = 10.0
R2 = 10.0
L1 = 15.0 * 10**(-3)
L2 = 15.0 * 10**(-3)
C1 = 50.0 * 10**(-6)
C2 = 50.0 * 10**(-6)
I1 = 12.0

#Parte real de Phi (a)
def a(w):
    a1 = R1
    a2 = -1.0*R1*L2*C1*(w**2)
    a3 = R2*L1*L2*C1*C2*(w**4)
    a4 = -1.0*R2*L1*C2*(w**2)
    a5 = -1.0*R2*L1*C1*(w**2)
    a6 = -1.0*R2*L2*C2*(w**2)
    a7 = R2
    ans = a1 + a2 + a3 + a4 + a5 + a6 + a7
    return ans

#Parte imaginaria de Phi (b)
def b(w):
    b1 = -1.0*R1*R2*L2*C1*C2*(w**2)
    b2 = R1*R2*C2*w
    b3 = R1*R2*C1*w
    b4 = w*L1
    b5 = -1.0*L1*L2*C1*(w**3)
    b6 = L2*w
    ans = b1 + b2 + b3 + b4 + b5 + b6
    return ans

#Magnitud de Vr2
def mag(a,w,b):
    up = I1*R1*R2
    down = np.sqrt((a(w)**2) + (b(w)**2))
    ans = up/(down*1.0)
    return ans

#Angulo de Vr2
def ang(a,w,b):
    e = b(w)/(a(w)*1.0)
    ans = -1.0*np.arctan(e)
    return ans

#Generar punto de w
ww = np.linspace(0,6000,1000)

#Puntos de w evaluados
mm = mag(a,ww,b)
aa = ang(a,ww,b)

#Grafica
plt.plot(ww,mm)
plt.title("Magnitud Vr2 vs. Frecuencia Angular")
plt.xlabel("Frecuencia angular (w) [rad/s]")
plt.ylabel("Magnitud [V]")
plt.savefig("Magnitud_Vr2.png")
plt.clf()
plt.plot(ww,aa)
plt.title("Fase Vr2 vs. Frecuencia Angular")
plt.xlabel("Frecuencia angular (w) [rad/s]")
plt.ylabel("Angulo de fase [rad]")
plt.savefig("Fase_Vr2.png")
plt.clf()
