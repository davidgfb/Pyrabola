from math import sqrt
from numpy import arange
from matplotlib.pyplot import plot, show, xlabel, ylabel

# y = -5x^2 + h

def devuelveY_X_PorX(x):
    return x * x

def devuelveY_Parabola(y, h, x):
    return -gMedios * y(x) + h

#PROBADOR
y, h, gMedios, ptosParabola = devuelveY_X_PorX, 1.5, 5, []

try:
    t = sqrt(h / gMedios)

except:
    t = 0 # si g = 0, t = inf (nunca cae)

xs = arange(0, t, 0.01)

for x in xs:
    ptoParabola = devuelveY_Parabola(y, h, x)
    
    ptosParabola.append(ptoParabola)
    
    #print("x =", round(x, 2), ", y =", ptoParabola)  

print("nPuntos =", len(xs)) # el nPuntos es dir prop a t = h. <g = vh
    
plot(xs, ptosParabola)
xlabel('t (s)')
ylabel('h (m)')
show()


