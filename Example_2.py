import numpy as np

class Robot_Arm:
    def __init__(self,DoF, angle):
        try:
            if DoF==3:
                self.m = 1
                self.x= [1.3, 2.5, -0.5]
            elif DoF==6:

                self.m = 1.5
                self.x = [1.2, -0.5, 0.9]
            self.x0 = self.RotX(angle)@self.x
        except AttributeError:
            print('DoF can be either 3 or 6')
            self.x0 = [1, 2, 3]
    def RotX(self, angle):
        R = np.array([[1, 0, 0], [0, np.cos(angle), -np.sin(angle)], [0, np.sin(angle), np.cos(angle)]])
        return R

DoF = 9
angle = np.pi/5

class_ra = Robot_Arm(DoF, angle)
print(class_ra.x0)

print(class_ra.RotX(np.pi/5))