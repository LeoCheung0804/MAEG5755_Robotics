import numpy as np
import tri as tr

sin, cos = tr.sind, tr.cosd
pi = np.pi

def T1(q):
    T = np.array([
        [cos(q), -sin(q), 0, 0],
        [sin(q), cos(q), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])
#   print(T)
    return T

def T2(q):
    T = np.array([
        [1, 0 , 0, 0],
        [0, cos(q), -sin(q), 0],
        [0, sin(q), cos(q),  a1],
        [0, 0, 0, 1]])
#    print(T)
    return T
def T3(q):
    T = np.array([
        [1, 0,0,0],
        [0, cos(q), -sin(q), l1],
        [0, sin(q), cos(q), -a2],
        [0, 0, 0, 1]])
#   print(T)
    return T
def R(l):
    R1 = np.array([
            [0],
            [l],
            [0],
            [1]])
    return R1
def FK(q1,q2,q3):
    T01 = T1(q1)


    T12 = T2(q2)
    T23 = T3(q3)
    R3 = R(l2)
    TX = T01 @ T12 @ T23 @ R3
    return TX

if __name__ == '__main__':
    # q = joint angle in degree
    q1 = -90
    q2 = 90
    q3 = -106
    a1 = 10.18
    l1 = 19.41
    a2 = 2.91
    l2 = 20.2
    TX= FK(q1, q2, q3)
print(TX)