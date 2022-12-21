import numpy as np
import tri as tr

sin, cos, tan = tr.sind, tr.cosd, tr.tand
asin, acos, atan = tr.asind, tr.acosd, tr.atand

pi = np.pi
l1 = 10.18
l2 = 19.63
l3 = 20.2

def get_ik(x_1, y_1, z_1):
    q1 = atan(-x_1, y_1)
    B = z_1 - l1
    p = ((x_1*x_1)+(y_1*y_1)+(B*B)-(l2*l2+l3*l3))/(2*l2*l3)
    q3 = acos(p)
    q3_1 = -q3
    a = l2+l3*cos(q3)
    b = l2*sin(q3)
    h = np.sqrt(a*a+b*b)
    c1 = a/h
    s1 = b/h
    gamma = atan(s1,c1)
    q2_1 = - gamma - asin(b/h)
    q2_2 = pi - gamma - asin(b/ h)
    m = [q1, q2_1 , q3]
    return m

if __name__ == '__main__':
    x = -17.7696
    y = 17.7696
    z = 29.6

    theta_0 = get_ik(x, y, z)
    print(theta_0)