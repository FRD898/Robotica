
import numpy as np
from matplotlib import pyplot as plt

def Trapezoidal2(q_i, q_f, a_max):
    '''
    Tiempo final: t_f
    Punto inicial y final: q_i, q_f
    Velocidad maxima: v_max 
    opcionales 
        Tiempo velocidad máxima : t_b
        Aceleración máxima: a_max 
    '''
    t_f = 2*((q_f - q_i)/a_max)**0.5
    t_s = t_f/2

    x = np.linspace(0.0001, t_f, 100)
    #position
    y = []
    for t in x:
        y.append(trapezoidalPosition2(t, q_i, q_f, t_s, a_max, t_f))
    GraphTrapezoidal2(f"T. Minimo \n Posicion tiempo:{0}-{t_f}",x, y)

    #velocidad
    y = []
    for t in x:
        y.append(trapezoidalSpeed2(t, t_s, a_max, t_f))
    GraphTrapezoidal2(f"T. Minimo \n Velocidad tiempo:{0}-{t_f}",x, y)

    #aceleracion
    y = []
    for t in x:
        y.append(trapezoidalAcceleration2(t, t_s, a_max, t_f))
    GraphTrapezoidal2(f"T. Minimo \n Aceleracion tiempo:{0}-{t_f}",x, y)
    return t_f
    
def GraphTrapezoidal2(title, x, y):
    plt.plot(x, y)
    plt.title(title)
    plt.show()



def trapezoidalPosition2(t, q_i, q_f, t_s, a_max, t_f):
    if t>0 and t<=t_s:
        q_t = q_i + 0.5*(a_max)*(t**2)
    elif t<= t_f:
        q_t = q_f - 0.5*a_max*(t-t_f)**2
    else:
        q_t = None
    return q_t

def trapezoidalSpeed2(t, t_s, a_max, t_f):
    if t>0 and t<=t_s:
        q_t = (a_max)*t
    elif t<=t_f:
        q_t = -(a_max)*(t-t_f)
    else:
        q_t = None
    return q_t

def trapezoidalAcceleration2(t, t_b, a_max, t_f):
    if t>0 and t<=t_b:
        q_t = (a_max)
    elif t<=t_f:
        q_t = -(a_max)
    else:
        q_t = None
    return q_t

def main():
    print("Probando archivo tiempoMinimo.py...")
    print(f'vel_i: 10°, vel_f: 60°, ac_max: 13.33 deg/s**2')
    Trapezoidal2(10, 60, 13.33)

if __name__=='__main__':
    main()
