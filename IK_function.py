import numpy as np
import tri as tr

sin, cos, tan = tr.sind, tr.cosd, tr.tand
asin, acos, atan = tr.asind, tr.acosd, tr.atand
pi = np.pi
l1 = 10.18
l2 = 19.63
l3 = 20.2

def get_ik(x, y, z):
    q1 = atan(-x, y)
    B = z - l1
    p = ((x*x+y*y)+(B*B)-(l3*l3+l2*l2))/(2*l2*l3)
    q3 = -acos(p)
    a = l1+l2*cos(q3)
    b = l1*sin(q3)
    h = np.sqrt(a*a+b*b)
    c1 = a/h
    s1 = b/h
    gamma = atan( c1, s1)
    q2_1 = gamma+asin(b/h)
    q2_2 = pi-gamma-asin(b/h)
    m = [q1, q2_1 , q3]
    return m

if __name__ == '__main__':
    x = 23.77
    y =  0
    z = 11.898
    m = get_ik(x,y,z)
    q1 = m[0]
    q2 = m[1]
    q3 = m[2]
    print(m)





