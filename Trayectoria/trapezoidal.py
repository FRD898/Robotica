
import numpy as np
from matplotlib import pyplot as plt

def Trapezoidal(t_f, q_i, q_f, v_max, t_b = None, a_max = None):
    '''
    Tiempo final: t_f
    Punto inicial y final: q_i, q_f
    Velocidad maxima: v_max 
    opcionales 
        Tiempo velocidad máxima : t_b
        Aceleración máxima: a_max 
    '''
    if a_max != None and a_max !=0:
        t_b = v_max/a_max
    elif t_b == None:
        t_b = (q_i - q_f + v_max*t_f)/v_max

    x = np.linspace(0.0001, t_f, 100)
    #position
    y = []
    for t in x:
        y.append(trapezoidalPosition(t, q_i, q_f, t_b, v_max, t_f))
    GraphTrapezoidal(f"Trapezoidal \n Posicion tiempo:{0}-{t_f}",x, y)

    #velocidad
    y = []
    for t in x:
        y.append(trapezoidalSpeed(t, t_b, v_max, t_f))
    GraphTrapezoidal(f"Trapezoidal \n Velocidad tiempo:{0}-{t_f}",x, y)

    #aceleracion
    y = []
    for t in x:
        y.append(trapezoidalAcceleration(t, t_b, v_max, t_f))
    GraphTrapezoidal(f"Trapezoidal \n Aceleracion tiempo:{0}-{t_f}",x, y)

    
def GraphTrapezoidal(title, x, y):
    plt.plot(x, y)
    plt.title(title)
    plt.show()



def trapezoidalPosition(t, q_i, q_f, t_b, v_max, t_f):
    if t>0 and t<=t_b:
        q_t = q_i + 0.5*(v_max/t_b)*(t**2)
    elif t<= t_f - t_b:
        q_t = q_i - 0.5*t_b*v_max + v_max*t
    elif t<=t_f:
        q_t = q_f - 0.5*(v_max/t_b)*(t-t_f)**2
    else:
        q_t = None
    return q_t

def trapezoidalSpeed(t, t_b, v_max, t_f):
    if t>0 and t<=t_b:
        q_t = (v_max/t_b)*t
    elif t<= t_f - t_b:
        q_t = v_max
    elif t<=t_f:
        q_t = -(v_max/t_b)*(t-t_f)
    else:
        q_t = None
    return q_t

def trapezoidalAcceleration(t, t_b, v_max, t_f):
    if t>0 and t<=t_b:
        q_t = (v_max/t_b)
    elif t<= t_f - t_b:
        q_t = 0
    elif t<=t_f:
        q_t = -(v_max/t_b)
    else:
        q_t = None
    return q_t

def main():
    Trapezoidal(4, 10, 60, 20)

if __name__ == '__name':
    main()


#GraphQuintico(2,4,10,60,0,0,0,0)
#GraphPolynom("Polinomio Cúbico",pol_Cubico(2,4,10,60,0,0), 2, 4)
#GraphPolynom("Polinomio Quintico",pol_Quintico(2,4,10,60,0,0,0,0), 2, 4)
#print(pol_Quintico(2,4,10,60,0,0,0,0)) 