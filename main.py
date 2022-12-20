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
    q3 = acos(((x_1 * x_1 + y_1 * y_1) + (B * B) - (l2 * l2 + l3 * l3)) / (2 * l2 * l3))
    a = l2 + l3 * cos(q3)
    b = l2 * sin(q3)
    h = np.sqrt(a * a + b * b)
    c1 = a / h
    s1 = b / h
    gamma = atan(s1, c1)
    q2_1 = - gamma + asin(B / h)
    q2_2 = pi - gamma - asin(B / h)
    m = [q1, q2_1 + 8.5, q3 - 8.5]
    return m

class Trajectory_linear(object):
    def __init__(self, _init_theta, _end_theta, t_f):

        self.init_theta = _init_theta
        self.end_theta = _end_theta
        self.num_joints = len(_init_theta)
        self.frequency = 50  # server update frequency
        self.t_f = t_f
        self.x_min = [-100, -100, -140]
        self.x_max = [100, 180, 100]
        assert len(_init_theta) == len(_end_theta), 'DoF doesnt match! '
        ### TODO: calculate paramenter self.k and self.b for each joint
        self.k = [(self.end_theta[i] - self.init_theta[i]) / t_f for i in range(self.num_joints)]
        self.b = [self.init_theta[i] for i in range(self.num_joints)]
        self.offset = [0, 0, 0]

    def get_angles(self, t):
        angles = []
        ### TODO: get angle for each joint
        angles = [self.k[i] * t + self.b[i] for i in range(self.num_joints)]
        return angles
        #print(angles)

    def get_whole_traj(self):
        angle_list = [[] for i in range(self.num_joints)]
        increment_t = 1 / self.frequency
        ticks = np.arange(0.0, self.t_f, increment_t)
        for t in ticks:
            angles = self.get_angles(t)
            for i in range(self.num_joints):
                angle = angles[i] + self.offset[i]
                if angle < self.x_min[i] or angle > self.x_max[i]:
                    raise Exception("out of range!")
                angle_list[i].append(angles[i])
        return angle_list


Task_x_0 = 0
Task_y_0 = 39.6
Task_z_0 = 7.27
Task_x_f = 30
Task_y_f = 0
Task_z_f = 7.56

t_f = 3

if __name__ == '__main__':
    theta_0 = get_ik(Task_x_0, Task_y_0, Task_z_0)
    print(theta_0)
    theta_f = get_ik(Task_x_f,Task_y_f,Task_z_f)
    print(theta_f)
    whole_traj = Trajectory_linear(theta_0, theta_f, t_f).get_whole_traj()
    return_str = 'angle;'
    for trajectory in whole_traj:
        return_str += ",".join([str(i) for i in trajectory]) + ";"
    print(return_str)
    with open('linear_trajectory.txt', 'w') as f:
        f.write(return_str)
