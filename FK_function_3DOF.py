import numpy as np

sin, cos = np.sin, np.cos
pi = np.pi
#initial parameter
#[j0 j1 j2 j3;d0 d1 d2 d3;a0 a1 a2 a3;t0 t1 t2 t3]


def dh(theta, d, a, alpha):
    dhm = np.array([
    [cos(theta),-sin(theta),0,a],
    [sin(theta)*cos(alpha),-cos(theta)*cos(alpha),-sin(alpha),-d*sin(alpha)],
    [sin(theta)*sin(alpha),cos(theta)*sin(alpha),cos(alpha),d*cos(alpha)],
    [0,0,0,1]])
    return dhm

def dhm(j1,j2,j3):
    alpha1 = j1
    alpha2 = j2
    alpha3 = j3
    alpha4 = 0
    a1 = 0
    a2 = 0
    a3 = 19.63
    a4 = 20.2
    d1 = 10.18
    d2 = 0
    d3 = 0
    d4 = 0
    theta1 = pi/4
    theta2 = pi/2
    theta3 = 0
    theta4 = 0
    T01 = dh(alpha1, a1, d1, theta1)
    T12 = dh(alpha2, a2, d2, theta2)
    T23 = dh(alpha3, a3, d3, theta3)
    T34 = dh(alpha4, a4, d4, theta4)
    dhmx = T01 @ T12 @ T23 @ T34
    return dhmx

if __name__ == '__main__':
    j1 = pi/4
    j2 = pi/2
    j3 = 0
    Tm = dhm(j1,j2,j3)
    print(Tm)