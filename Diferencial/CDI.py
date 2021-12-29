#Halla las velocidades articulares necesarias para que alguna parte del robot
#obtenga una velocidad instantánea determinada
import sympy as sp

def JA_RRR():
    q1, q2, q3, L1, L2, L3 = sp.symbols("q1 q2 q3 L1 L2 L3")

    # Cinemática directa
    x = L1*sp.cos(q1) + L2*sp.cos(q1+q2) + L3*sp.cos(q1+q2+q3)
    y = L1*sp.sin(q1) + L2*sp.sin(q1+q2) + L3*sp.sin(q1+q2+q3)
    th = q1 + q2 + q3

    X = sp.Matrix([x, y, th])
    q = sp.Matrix([q1, q2, q3])

    # Jacobiano analítico
    Ja = X.jacobian(q)
    return Ja
def test():
    q1, q2, q3, L1, L2, L3 = sp.symbols("q1 q2 q3 L1 L2 L3")
    Ja = JA_RRR()
    # Configuración
    qd = [sp.pi/4, -sp.pi/4, -sp.pi/4]

    # Reemplazando valores en el Jacobiano
    J = Ja.subs({q1: qd[0], q2: qd[1], q3: qd[2], L1:0.5, L2:1, L3:0.5})
    print(J)

def Pseudoinversa1(J):
    #n>m
    return J.T*((J*J.T).inv)

def Pseudoinversa2(J):
    #m>n
    return ((J*J.T).inv)*J.T

def main():
    test()

if __name__ == '__main__':
    main()