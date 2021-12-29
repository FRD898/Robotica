import numpy as np
from matplotlib import pyplot as plt


def polinomio3(t_i, t_f, q_i, q_f, v_i, v_f):
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

def polinomio4(t_i, t_f, q_i, q_f, v_i, v_f, a_i, a_f):
    '''
    Esta función permite calcular a_i
    t_i,t_f = Tiempo inicial y final 
    q_0,q_f = Punto inicial y final 
    v_i, v_f = Velocidad inicial y final
    a_i, a_f = Aceleracion inicial y final
    '''
    A = np.array([[t_i**4,t_i**3,t_i**2,t_i**1,1], 
                [t_f**4,t_f**3,t_f**2,t_f**1,1], 
                [4*t_i**3,3*t_i**2,2*t_i**1,1,0], 
                [4*t_f**3,3*t_f**2,2*t_f**1,1,0],
                [12*t_i**2, 6*t_i, 2,   0,  0],
                [12*t_f**2, 6*t_f, 2,0,0]])
    b = np.array([q_i, q_f, v_i, v_f, a_i, a_f])
    x = np.linalg.solve(A, b)
    return x

def Polinomial434(t_0,t_1,t_2,t_f, q_0,q_1,q_2,q_f,v_1,v_2,a_1,a_2):
    tramo1 = polinomio4(t_0, t_1, q_0, q_1, 0, v_1, 0, a_1)
    tramo2 = polinomio3(t_1, t_2, q_1, q_2, v_1, v_2)
    tramo3 = polinomio4(t_2, t_f, q_2, q_f, v_2, 0, a_2, 0)

def main():
    pass

if __name__ == '__main__':
    main()