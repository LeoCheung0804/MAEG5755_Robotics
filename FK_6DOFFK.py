import numpy as np
import tri as tr

sin, cos, tan = tr.sind, tr.cosd, tr.tand
asin, acos, atan = tr.asind, tr.acosd, tr.atand
pi = np.pi
a1 = 10.18
a2 = 2.91
l1 = 19.41
l2 = 25.22
l3 = 3

def T1(q):
    T = np.array([
        [cos(q), -sin(q), 0, 0],
        [sin(q), cos(q), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])
    return T
def T2(q):
    T = np.array([
        [1, 0, 0, 0],
        [0, cos(q), -sin(q), 0],
        [0, sin(q), cos(q),  a1],
        [0, 0, 0, 1]])
#    print(T)
    return T
def T3(q):
    T = np.array([
        [1, 0, 0, 0],
        [0, cos(q), -sin(q), l1],
        [0, sin(q), cos(q), -a2],
        [0, 0, 0, 1]])
#   print(T)
    return T
def T4(l2):
    T = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, l2],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])
    return T
def T5(q):
    T = np.array([
        [cos(q), 0, sin(q), 0],
        [0, 1, 0, 0],
        [-sin(q), 0, cos(q), 0],
        [0, 0, 0, 1]])
    return T
def T6(q):
    T = np.array([
        [1, 0, 0, 0],
        [0, cos(q), -sin(q), 0],
        [0, sin(q), cos(q), 0],
        [0, 0, 0, 1]])
    return T
def T7(q):
    T = np.array([
        [cos(q), -sin(q), 0, 0],
        [sin(q), cos(q), 0, 0],
        [0, 0, 1, l3],
        [0, 0, 0, 1]])
    return T
def get_last_three_angles(R):
    cos_q5 = R[2,2]
    q5 = acos(cos_q5)
    sin_q5 = sin(q5)
    sin_q6 = (R[1,2])/sin_q5
    q6 = asin(sin_q6)
    cos_q4 = R[2,0]/sin_q5
    q4 = acos(cos_q4)

    m = [q4,q5,q6]
    return m

if __name__ == '__main__':
        # q = joint angle in degree
        q1 = 45
        q2 = 90
        q3 = -90
        q4 = 180
        q5 = 90
        q6 = 90
        T01 = T1(q1)
        T12 = T2(q2)
        T23 = T3(q3)
        T34 = T4(l2)
        T45 = T5(q4)
        T56 = T6(q5)
        T67 = T7(q6)
        T03 = T01 @ T12 @ T23 @ T34
        T36 = T45 @ T56 @ T67
        T = T03 @ T36
        ABG = get_last_three_angles(T)
        print(T)
        x = T[0,3]
        y = T[1,3]
        z = T[2,3]
        print(x)
        print(y)
        print(z)
        print(ABG)

