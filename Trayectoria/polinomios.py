import numpy as np
from matplotlib import pyplot as plt

def pol_Cubico(t_i, t_f, q_i, q_f, v_i, v_f):
    '''
    Esta función permite calcular a_i
    t_i,t_f = Tiempo inicial y final 
    q_0,q_f = Punto inicial y final 
    v_i, v_f = Velocidad inicial y final
    '''
    A = np.array([[t_i**3, t_i**2, t_i, 1], [t_f**3, t_f**2, t_f, 1], [3*t_i**2, 2*t_i, 1, 0], [3*t_f**2, 2*t_f, 1, 0]])
    b = np.array([q_i, q_f, v_i, v_f])
    x = np.linalg.solve(A, b)
    return x

def pol_Quintico(t_i, t_f, q_i, q_f, v_i, v_f, a_i, a_f):
    '''
    Esta función permite calcular a_i
    t_i,t_f = Tiempo inicial y final 
    q_0,q_f = Punto inicial y final 
    v_i, v_f = Velocidad inicial y final
    a_i, a_f = Aceleración inicial y final
    '''
    A = np.array([[t_i**5,t_i**4, t_i**3, t_i**2, t_i, 1], 
                [t_f**5, t_f**4, t_f**3, t_f**2, t_f, 1], 
                [5*t_i**4, 4*t_i**3, 3*t_i**2, 2*t_i, 1, 0], 
                [5*t_f**4, 4*t_f**3, 3*t_f**2, 2*t_f, 1, 0],
                [20*t_i**3, 12*t_i**2, 6*t_i, 2, 0, 0],
                [20*t_f**3, 12*t_f**2, 6*t_f, 2, 0, 0]])
    b = np.array([q_i, q_f, v_i, v_f, a_i, a_f])
    x = np.linalg.solve(A, b)
    return x


def PolyCoefficients(x, coeffs):
    """ x: puntos de interpolacion
        coefs: coeficientes del polinomio f(x)
        return: arreglo de f(x_i)
    """
    o = len(coeffs)
    print(f'# This is a polynomial of order {ord}.')
    y = 0
    for i in range(o):
        y += coeffs[-(i+1)]*x**i
    return y

def GraphPolynom(title, coeffs, t_i, t_f):
    x = np.linspace(t_i, t_f, 100)
    plt.plot(x, PolyCoefficients(x, coeffs))
    plt.title(f'{title} \n (tiempo : {t_i} - {t_f})')
    plt.show()

def GraphCubico(t_i, t_f, q_i, q_f, v_i, v_f):
    coeffs = pol_Cubico(t_i, t_f, q_i, q_f, v_i, v_f) #4
    #Posicion 
    GraphPolynom("Posición - Polinomio Cúbico ", coeffs, t_i, t_f)
    #Velocidad 
    vel = [3*coeffs[0], 2*coeffs[1], coeffs[2]]
    GraphPolynom("Velocidad - Polinomio Cúbico", vel, t_i, t_f)
    #Aceleracion
    ac = [6*coeffs[0], 2*coeffs[1]]
    GraphPolynom("Aceleración - Polinomio Cúbico", ac, t_i, t_f)

def GraphQuintico(t_i, t_f, q_i, q_f, v_i, v_f, a_i, a_f):
    #Posicion
    coeffs =  pol_Quintico(t_i, t_f, q_i, q_f, v_i, v_f, a_i, a_f) #6
    GraphPolynom("Polinomio Quintico",coeffs, t_i, t_f)
    #Velocidad 
    vel = [5*coeffs[0], 4*coeffs[1], 3*coeffs[2], 2*coeffs[3], coeffs[4]]
    GraphPolynom("Velocidad - Polinomio Quintico", vel, t_i, t_f)
    #Aceleracion
    ac = [20*coeffs[0], 12*coeffs[1], 6*coeffs[2], 2*coeffs[3]]
    GraphPolynom("Aceleración - Polinomio Quintico", ac, t_i, t_f)

def main():
    print("Probando archivo polinomios.py...")
    print(f'vel_i: 10°, vel_f: 60°, t_i: 2, t_f: 4')
    GraphCubico(2,4,10,60,0,0)
    GraphQuintico(2,4,10,60,0,0,0,0)

if __name__ == '__main__':
    main()