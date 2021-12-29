import sympy as sp
from CD.rotaciones import *
def sVectorFromSkew(S):
    return sp.Matrix([S[2,1],S[0,2],S[1,0]])

def get_W_hat(R, dRdt, dt):
    return sp.simplify( dRdt * dt * R.T)

def get_v_p(w,p,v_b):
    return w.cross(p) + v_b

def RPY():
    r, p, y, dr, dp, dy = sp.symbols("r p y dr dp dy")
    # Componente de velocidad debido a "roll"
    wr = sp.Matrix([0,0,1])*dr

    # Componente de velocidad debido a "pitch"
    Rz = srotz(r)
    wp = Rz[:,1]*dp

    # Componente de velocidad debido a "yaw"
    Rrp = sp.simplify(srotz(r)*sroty(p))
    wy = Rrp[:,0]*dy

    # Velocidad angular
    w = wr + wp + wy
    print(w)


def test():
    t, dt = sp.symbols("t dt")
    # Matriz de rotación
    R = sroty(t)
    # Derivada con respecto al ángulo t
    dRdt = sp.diff(R,t)
    # Matriz antisimétrica
    w_hat = get_W_hat(R, dRdt, dt)
    print(w_hat)
    print(sVectorFromSkew(w_hat))

    #alcular la relación entre las derivadas de los ángulos de roll, pitch, yaw con la velocidad angular
    r,p,y,dr,dp,dy = sp.symbols("r p y dr dp dy")
    R = sp.simplify(srotz(r)*sroty(p)*srotx(y))
    dRdt = sp.simplify(sp.diff(R,r)*dr + sp.diff(R,p)*dp + sp.diff(R,y)*dy)
    w_hat = sp.simplify(dRdt*R.T)
    w = sVectorFromSkew(w_hat)
    print(f"w_hat: {w_hat}")
    print(f"w: {w}")

def main():
    test()

if __name__ == '__main__':
    main()