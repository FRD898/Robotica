import numpy as np
from matplotlib import pyplot as plt

def splines3(t_0,t_1, q_0,q_1, v_0,v_1):
    t1 = 0; q1 = 0; dq1 = 0
    t2 = 2; q2 = 2*np.pi
    t3 = 3; q3 = np.pi/2
    t4 = 5; q4 = np.pi; dq4 = 0

    # Se formará el sistema Ab = X para encontrar las variables ai, bi, ci contenidas en X
    # EL orden de elementos en X es: [a0, a1, a2, a3, b0, b1, b2, b3, c0, c1, c2, c3]

    A = np.array([
        [1, t1, t1**2,   t1**3, 0,  0,     0,        0, 0,  0,     0,        0],
        [1, t2, t2**2,   t2**3, 0,  0,     0,        0, 0,  0,     0,        0],
        [0,  0,     0,       0, 1, t2, t2**2,    t2**3, 0,  0,     0,        0],
        [0,  0,     0,       0, 1, t3, t3**2,    t3**3, 0,  0,     0,        0],
        [0,  0,     0,       0, 0,  0,     0,        0, 1, t3, t3**2,    t3**3],
        [0,  0,     0,       0, 0,  0,     0,        0, 1, t4, t4**2,    t4**3],
        [0,  1,  2*t1, 3*t1**2, 0,  0,     0,        0, 0,  0,     0,        0],
        [0,  0,     0,       0, 0,  0,     0,        0, 0,  1,  2*t4,  3*t4**2],
        [0,  1,  2*t2, 3*t2**2, 0, -1, -2*t2, -3*t2**2, 0,  0,     0,        0],
        [0,  0,     0,       0, 0,  1,  2*t3,  3*t3**2, 0, -1, -2*t3, -3*t3**2],
        [0,  0,     2,    6*t2, 0,  0,    -2,    -6*t2, 0,  0,     0,        0],
        [0,  0,     0,       0, 0,  0,     2,     6*t3, 0,  0,    -2,    -6*t3]
    ])

    b = np.array([[q1, q2, q2, q3, q3, q4, dq1, dq4, 0, 0, 0, 0]]).T

    X = np.dot(np.linalg.inv(A), b)
    print(X.T)

    # Polinomio 1
    a0 = X[0]; a1 = X[1]; a2 = X[2]; a3 = X[3]
    # Polinomio 2
    b0 = X[4]; b1 = X[5]; b2 = X[6]; b3 = X[7]
    # Polinomio 3
    c0 = X[8]; c1 = X[9]; c2 = X[10]; c3 = X[11]

    # Recuperación de los polinomios (por partes)

    # Polinomio 1
    ta = np.linspace(t1, t2, 50)
    qa = a3*ta**3 + a2*ta**2 + a1*ta + a0
    dqa = 3*a3*ta**2 + 2*a2*ta + a1
    ddqa = 6*a3*ta + 2*a2

    # Polinomio 2
    tb = np.linspace(t2, t3, 50)
    qb = b3*tb**3 + b2*tb**2 + b1*tb + b0
    dqb = 3*b3*tb**2 + 2*b2*tb + b1
    ddqb = 6*b3*tb + 2*b2

    # Polinomio 3
    tc = np.linspace(t3, t4, 50)
    qc = c3*tc**3 + c2*tc**2 + c1*tc + c0
    dqc = 3*c3*tc**2 + 2*c2*tc + c1
    ddqc = 6*c3*tc + 2*c2

    # Vectores que contienen todo el intervalo de tiempo
    t = np.hstack((ta, tb, tc))
    q = np.hstack((qa, qb, qc))
    dq = np.hstack((dqa, dqb, dqc))
    ddq = np.hstack((ddqa, ddqb, ddqc))

    plt.figure(figsize=(15,5))

    # Posición
    plt.subplot(1,3,1); plt.plot(t, q); 
    plt.plot([t1, t2, t3, t4], [q1, q2, q3, q4], 'o')
    plt.title("Posición"); plt.xlabel("t [s]"); plt.ylabel("[rad]")
    plt.grid()

    # Velocidad
    plt.subplot(1,3,2); plt.plot(t, dq)
    plt.plot([t1, t4], [dq1, dq4], 'o')
    plt.title("Velocidad"); plt.xlabel("t [s]"); plt.ylabel("[rad/s]")
    plt.grid()

    plt.subplot(1,3,3); plt.plot(t, ddq)
    plt.title("Aceleración"); plt.xlabel("t [s]"); plt.ylabel("[rad/$s^2$]")
    plt.grid()

def main():
    splines3()

if __name__ == '__main__':
    main()