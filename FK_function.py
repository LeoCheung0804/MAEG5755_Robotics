# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import math
import tri as tr

def dh(theta,d,a,alpha):
    dhm = np.array([[tr.cosd(theta), -tr.sind(theta), 0, a],
    [tr.sind(theta)*tr.cosd(alpha), -tr.sind(theta), -tr.sind(alpha)*d],
    [tr.sind(theta)*tr.sind(alpha), tr.cosd(theta)*tr.sind(alpha), tr.cosd(alpha), d*tr.cosd(alpha)],
    [0,0,0,1]])
    return dhm

if __name__ == '__main__':
    theta = 90.0
    d = 10.0
    a = 1.0
    alpha = 20.0
    dhm = dh(theta,d,a,alpha)
    print(dhm)
