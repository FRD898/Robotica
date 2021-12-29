#Usa la razón de cambio (derivada) de la posición y de la orientación
import sympy as sp
def Jacobiano_A():
    q1, q2, l1, l2 = sp.symbols("q1 q2 l1 l2")

    # Forma 1
    # =======

    # Cinemática directa (término a término)
    x = l1*sp.cos(q1) + l2*sp.cos(q1+q2)
    y = l1*sp.sin(q1) + l2*sp.sin(q1+q2)
    phi = q1 + q2

    # Derivadas (término a término)
    dxdq1 = sp.diff(x, q1) 
    dxdq2 = sp.diff(x, q2)
    dydq1 = sp.diff(y, q1) 
    dydq2 = sp.diff(y, q2)
    dphidq1 = sp.diff(phi, q1) 
    dphidq2 = sp.diff(phi, q2)

    # Jacobiano analitico
    Ja1 = sp.Matrix([[  dxdq1,   dxdq2],
                    [  dydq1,   dydq2],
                    [dphidq1, dphidq2]])    
    return Ja1

def Jacobiano_A2():
    q1, q2, l1, l2 = sp.symbols("q1 q2 l1 l2")
    X = sp. Matrix([[ l1*sp.cos(q1) + l2*sp.cos(q1+q2)],
                [ l1*sp.sin(q1) + l2*sp.sin(q1+q2)],
                [ q1 + q2]])

    # Vector de variables articulares
    q = sp.Matrix([q1,q2])

    # Jacobiano analítico (usando la función "jacobian")
    Ja1 = X.jacobian(q)
    return Ja1

def test():
    print(Jacobiano_A())
    print(Jacobiano_A2())

def main():
    test()

if __name__ == '__main__':
    main()