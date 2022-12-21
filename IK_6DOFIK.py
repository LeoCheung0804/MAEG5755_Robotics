import numpy as np
import tri as tr

sin, cos, tan = tr.sind, tr.cosd, tr.tand
asin, acos, atan = tr.asind, tr.acosd, tr.atand
pi = np.pi

a1=10.18
l1=19.63
l2=25.22
l3=3

def Euler(M, N, L):
    Rz1=np.array([
        [cos(M), -sin(M), 0, 0],
        [sin(M), cos(M), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])
    Ry2=np.array([
        [cos(N), 0, sin(N), 0],
        [0, 1, 0, 0],
        [-sin(N), 0, cos(N), 0],
        [0, 0, 0, 1]])
    Rz3=np.array([
        [cos(L), -sin(L), 0, 0],
        [sin(L), cos(L), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])
    R = Rz1 @ Ry2 @ Rz3
    return R

def T(x_1,y_1,z_1):
    T = np.array([[x_1],[y_1],[z_1],[1]])-Euler(M,N,L)*np.array([[0],[l3],[z_1],[1]])
    xre=T[0,0]
    yre=T[1,0]
    zre=T[2,0]
    return xre,yre,zre

def get_ik03(x, y, z):
    q1 = atan(-x, y)
    B = z - a1
    p = ((x*x+y*y)+B*B-(l1*l1+l2*l2))/(2*l1*l2)
    q3 = acos(p)
    a = l1 + l2 * cos(q3)
    b = l1 * sin(q3)
    h = np.sqrt(a * a + b * b)
    c1 = a / h
    s1 = b / h
    gamma = atan(s1, c1)
    q2_1 = - gamma - asin(b / h)
    q2_2 = pi - gamma - asin(b / h)
    m = [q1, q2_1 , q3]
    return m

def getT03(q1,q2,q3):
    T1 = np.array([
        [cos(q1), - sin(q1), 0, 0],
        [sin(q1), cos(q1), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])
    T2 =  np.array([
        [1, 0, 0, 0],
        [0, cos(q2), - sin(q2), 0],
        [0, sin(q2), cos(q2), a1],
        [0, 0, 0, 1]])
    T3 = np.array([
        [1, 0, 0, 0],
        [0, cos(q3), - sin(q3), l1],
        [0, sin(q3), cos(q3), 0],
        [0, 0, 0, 1]])
    T4 = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, l2],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])

    T03 = T1 @ T2 @ T3 @ T4
    return T03

def getR03(A):
    R = A[0:3,0:3]
    return R
def R03_inv(M):
    R = np.linalg.inv(M)
    return R
def Re(E):
    M = E[0:3,0:3]
    return M

def getT36(q4,q5,q6):
    T5 =np.array([
        [cos(q4), 0, sin(q4), 0],
        [0, 1, 0, 0],
        [-sin(q4), 0 ,cos(q4), 0],
        [0, 0, 0, 1]])
    T6 = np.array([
        [1, 0, 0, 0],
        [0, cos(q5), - sin(q5), l1],
        [0, sin(q5), cos(q5), 0],
        [0, 0, 0, 1]])
    T7 = np.array([
        [cos(q6), -sin(q6), 0, 0],
        [sin(q6) ,cos(q6), 0, 0],
        [0, 0, 1, l3],
        [0, 0, 0, 1]])
    T36 = T5 @ T6 @ T7

    return T36

def get_last_three_angles(R):
    sin_q4 = R[2, 2]
    cos_q4 = -R[0, 2]

    sin_q5 = np.sqrt(R[0, 2] ** 2 + R[2, 2] ** 2)
    cos_q5 = R[1, 2]

    sin_q6 = -R[1, 1]
    cos_q6 = R[1, 0]

    q4 = atan(sin_q4, cos_q4)
    q5 = atan(sin_q5, cos_q5)
    q6 = atan(sin_q6, cos_q6)
    m = [q4,q5,q6]
    return m



if __name__ == '__main__':
    x_1 = -17.7696
    y_1 = 17.7696
    z_1 = 29.6
    M = 0
    N = -45
    L = 90
    point = x_1,y_1,z_1
    a = Euler(M,N,L)

    T = T(x_1, y_1, z_1)

    J_03 = get_ik03(x_1,y_1,z_1)
    print(J_03)
    T03 = getT03(J_03[0],J_03[1],J_03[2])

    R03 = getR03(T03)

    R03_inv = R03_inv(R03)

    Re = Re(a)

    R36 = R03_inv*Re

    J46 = get_last_three_angles(R36)
    print(J46)









