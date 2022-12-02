import numpy as np

class Trajectory_linear(object):
    def __init__(self, _init_theta, _end_theta, t_f):

        self.init_theta = _init_theta
        self.end_theta = _end_theta
        self.num_joints = len(_init_theta)
        self.frequency = 50 # server update frequency
        self.t_f = t_f
        self.angle_min = [-90, -15, -180]
        self.angle_max = [90, 180, 10]
        assert len(_init_theta) == len(_end_theta), 'DoF doesnt match! '
        ### TODO: calculate paramenter self.k and self.b for each joint theta =𝑘𝑡+𝑏
        self.k = (_end_theta - _init_theta)/(t_f)
        self.b = (_init_theta)
        self.offset = 0



    def get_angles(self, t):
       angles = []
        ### TODO: get angle for each joint
        angles = angle

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


angle = np.array(theta)
Rxyz = RotXYZ(angle)
print(Rxyz)

    def get_whole_traj(self):
        angle_list = [[] for i in range(self.num_joints)]

        increment_t = 1/self.frequency
        ticks = np.arange(0.0,self.t_f, increment_t)
        for t in ticks:
            angles =  self.get_angles(t)
            for i in range(self.num_joints):
                angle = angles[i] + self.offset[i]
                if angle<self.angle_min[i] or angle > self.angle_max[i]:
                    raise Exception("out of range!")
                angle_list[i].append(angles[i])
        return angle_list

theta_0 = [0, 0, 0]
theta_f = [10, 10, 10]
t_f = 3
if __name__ == '__main__':
    whole_traj = Trajectory_linear(theta_0, theta_f, t_f).get_whole_traj()
    return_str = 'angle;'
    for trajectory in whole_traj:
        return_str += ",".join([str(i) for i in trajectory]) + ";"
    print(return_str)
    with open('linear_trajectory.txt', 'w') as f:
        f.write(return_str)


