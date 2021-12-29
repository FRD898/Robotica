import sympy as sp            
import numpy as np
from numpy import array, sin, cos
def rotX(theta):
    return array([[1,          0,           0],
                   [0, cos(theta), -sin(theta)],
                   [0, sin(theta), cos(theta)]])
# rotacion alrededor del eje y
def rotY(theta):
    return array([[ cos(theta), 0, sin(theta)],
                   [          0, 1,          0],
                   [-sin(theta), 0, cos(theta)]])
# rotacion alrededor del eje z    
def rotZ(theta):
    return array([[cos(theta), -sin(theta), 0],
                   [sin(theta), cos(theta),  0],
                   [         0,          0,  1]])

def rotphX(theta):
    return array([[1,          0,           0, 0],
                   [0, cos(theta), -sin(theta), 0],
                   [0, sin(theta), cos(theta),  0],
                   [0,          0,          0,  1]])

def rotphY(theta):
    return array([[ cos(theta), 0, sin(theta), 0],
                   [          0, 1,          0, 0],
                   [-sin(theta), 0, cos(theta), 0],
                   [0,           0,          0, 1]])
    
def rotphZ(theta):
    return array([[cos(theta), -sin(theta),  0,    0],
                   [sin(theta),  cos(theta),  0,    0],
                   [         0,           0,  1,    0],
                   [         0,           0,  0,    1]])

# Traslaciones puras:
def traslphX(d):
    return array([[1,  0,  0,  d],
                   [0,  1,  0,  0],
                   [0,  0,  1,  0],
                   [0,  0,  0,  1]])

def traslphY(d):
    return array([[1,  0,  0,  0],
                   [0,  1,  0,  d],
                   [0,  0,  1,  0],
                   [0,  0,  0,  1]])
def traslphZ(d):
    return array([[1,  0,  0,  0],
                   [0,  1,  0,  0],
                   [0,  0,  1,  d],
                   [0,  0,  0,  1]])

#Transformaciones desde DH
#Usando numpy
def Tdh(d, th, a, alpha):
    cth = np.cos(th);    sth = np.sin(th)
    ca = np.cos(alpha);  sa = np.sin(alpha)
    Tdh = np.array([[cth, -ca*sth,  sa*sth, a*cth],
                    [sth,  ca*cth, -sa*cth, a*sth],
                    [0,        sa,     ca,      d],
                    [0,         0,      0,      1]])
    return Tdh



#Usando sympy
def srotx(ang):
    """ Matriz de rotación alrededor de x
    """
    Rx = sp.Matrix([[1, 0, 0],
                    [0, sp.cos(ang), -sp.sin(ang)],
                    [0, sp.sin(ang), sp.cos(ang)]])
    return Rx

def sroty(ang):
    """ Matriz de rotación alrededor de y
    """
    Ry = sp.Matrix([[sp.cos(ang), 0, sp.sin(ang)],
                    [0, 1, 0],
                    [-sp.sin(ang), 0, sp.cos(ang)]])
    return Ry

def srotz(ang):
    """ Matriz de rotación alrededor de z
    """
    Rz = sp.Matrix([[sp.cos(ang),-sp.sin(ang),0],
                    [sp.sin(ang), sp.cos(ang),0],
                    [0,0,1] ])
    return Rz
    
def sTdh(d, th, a, alpha):
    cth = sp.cos(th); sth = sp.sin(th)
    ca = sp.cos(alpha); sa = sp.sin(alpha)
    Tdh = sp.Matrix([[cth, -ca*sth,  sa*sth, a*cth],
                     [sth,  ca*cth, -sa*cth, a*sth],
                     [0,        sa,     ca,      d],
                     [0,         0,      0,      1]])
    return Tdh



# Cinemática directa del robot
def cdirecta_scara(q, l1, l2, l3, l4):
    """ Retorna los sistemas de referencia de cada eslabón con respecto a la base
    """
    # Transformaciones homogéneas de DH
    T01 = Tdh(       l1,    np.pi+q[0], l2,     0)
    T12 = Tdh(        0, -np.pi/2+q[1], l3,     0)
    T23 = Tdh( -l4+q[2],             0,  0,     0)
    T34 = Tdh(        0,  np.pi/2+q[3],  0, np.pi)
    # Efector final con respecto a la base
    Tf = T01.dot(T12).dot(T23).dot(T34)
    return Tf

    #De manera simbolica
    '''
    q1, q2, q3, q4 = sp.symbols("q1 q2 q3 q4")
    l1, l2, l3, l4 = sp.symbols("l1 l2 l3 l4")

    # Transformaciones homogéneas
    T01 = sTdh(    l1,    sp.pi+q1, l2,     0)
    T12 = sTdh(     0, -sp.pi/2+q2, l3,     0)
    T23 = sTdh(-l4+q3,           0,  0,     0)
    T34 = sTdh(     0,  sp.pi/2+q4,  0, sp.pi)

    # Transformación homogénea final
    Tf = sp.simplify(T01*T12*T23*T34)
    '''



def test():
    # Ejemplo de cálculo de la cinemática directa
    l1 = 1.0                               # Longitud eslabón 1
    l2 = 1.0                               # Longitud eslabón 2
    l3 = 1.0                               # Longitud eslabón 3 
    l4 = 0.5
    q = [np.deg2rad(0), np.deg2rad(0), 0, np.deg2rad(0)]    # Valores articulares

    # Cinemática directa
    Te = cdirecta_scara(q, l1, l2, l3, l4)   # Cinemática directa

    # Mostrar el resultado
    print("Efector final con respecto a la base cuando q1={}, q2={}, q3={}, q4={}".format(np.rad2deg(q[0]), np.rad2deg(q[1]), 
                                                                                        q[2], np.rad2deg(q[3])))
    print(np.round(Te,4))

def main():
    test()

if __name__ == '__main__':
    main()