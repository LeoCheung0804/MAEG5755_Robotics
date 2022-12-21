import numpy as np
import math

def tand(x):
    return np.tan(x * np.pi / 180)

def sind(x):
    return np.sin(x * np.pi / 180)

def cosd(x):
    return np.cos(x * np.pi / 180)

# arctan(y/x)
def atand(y, x):
    a = math.atan2(y, x) * 180 / np.pi
    return a

def asind(x):
    return np.arcsin(x) * 180 / np.pi

def acosd(x):
    return np.arccos(x) * 180 / np.pi

if __name__ == '__main__':
    x = 0.273
    y = acosd(x)
    print(y)