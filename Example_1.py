import numpy as np


def RotX(angle):
    R = np.array([[1, 0, 0], [0, np.cos(angle), -np.sin(angle)], [0, np.sin(angle), np.cos(angle)]])
    return R


def RotY(angle):
    R = np.array([[np.cos(angle), 0, np.sin(angle)], [0, 1, 0], [-np.sin(angle), 0, np.cos(angle)]])
    return R


def RotZ(angle):
    R = np.array([[np.cos(angle), -np.sin(angle), 0], [np.sin(angle), np.cos(angle), 0], [0, 0, 1]])
    return R


def RotXYZ(angle):
    Rx = RotX(angle[0])
    Ry = RotY(angle[1])
    Rz = RotZ(angle[2])
    # R = Rx.dot(Ry).dot(Rz)
    R = Rx @ Ry @ Rz
    return R


angle = [np.pi / 14, -np.pi / 6, np.pi / 4]
Rxyz = RotXYZ(angle)
print(Rxyz)


def Sin(T):
    N = T * 100 + 1  # This ensures dt = 0.01
    time = np.linspace(0, T, N)
    f = list(0 for i in range(0, N))
    for k in range(0, N):
        f[k] = np.sin(time[k])
    return f


f = [Sin(3)]
print(f)


