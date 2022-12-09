import numpy as np
import tri as tr
sin, cos, tan = tr.sind, tr.cosd, tr.tand
asin, acos, atan = tr.asind, tr.acosd, tr.atand

pi = np.pi

def q1(x, y):
    q = atan(-x/y)
    return q
def A(x,y,q):
    a = -x*sin(q)+y*cos(q)
    return a
def B(z):
    b = z-l1
    return b


if __name__ == '__main__':
    x = 2.82758347
    y = -2.82758347
    z = 48.57179094
    l1 = 10.18
    l2 = 19.63
    l3 = 20.2
    q = q1(x, y)
    q3 = acos((A(x,y,q)*A(x,y,q)+B(z)*B(z)-(l2*l2+l3*l3))/(2*l2*l3)) - 8.526
    q2 = atan(((B(z)*(l2+(l3*cos(q3)))-(A(x,y,q)*l3*sin(q3)))/(A(x,y,q)*(l2+l3*cos(q3))+B(z)*l3*sin(q3)))) + 8.526

print(q)
print(q2)
print(q3)
