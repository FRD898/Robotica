import sympy as sp
#Usa la velocidad lineal (v) y angular (ω) del efector final
def Jacobiano_G():
    q1,q2,l1,l2 = sp.symbols("q1 q2 l1 l2")

    # Matrices de transformación homogénea
    T01 = sp.Matrix([[sp.cos(q1), -sp.sin(q1), 0, l1*sp.cos(q1)],
                    [sp.sin(q1),  sp.cos(q1), 0, l1*sp.sin(q1)],
                    [         0,           0, 1,             0],
                    [         0,           0, 0,             1]])
    T12 = sp.Matrix([[sp.cos(q2), -sp.sin(q2), 0, l2*sp.cos(q2)],
                    [sp.sin(q2),  sp.cos(q2), 0, l2*sp.sin(q2)],
                    [         0,           0, 1,             0],
                    [         0,           0, 0,             1]])
    T02 = sp.simplify(T01*T12)

    # Ejes z con respecto al sistema 0
    z0 = sp.Matrix([[0],[0],[1]]); 
    z1 = T01[0:3, 2]
    # Puntos con respecto al sistema 0
    p0 = sp.Matrix([[0],[0],[0]]); 
    p1 = T01[0:3, 3]; 
    p2 = T02[0:3, 3]; 

    #Componentes de los jacobianos para prismatica
    '''Jv1 = z0; 
    Jv2 = z1; 
    Jw1 = 0; 
    Jw2 = 0'''

    # Componentes de los Jacobianos(revolucion)
    Jv1 = z0.cross(p2-p0); 
    Jv2 = z1.cross(p2-p1); 
    Jw1 = z0; 
    Jw2 = z1

    # Jacobiano geométrico (columna a columna)
    J1 = sp.Matrix.vstack(Jv1, Jw1)
    J2 = sp.Matrix.vstack(Jv2, Jw2)
    # Jacobiano geométrico (completo)
    J = sp.Matrix.hstack(J1, J2)
    return J 

def test():
    print(Jacobiano_G())

def main():
    test()

if __name__ == '__main__':
    main()