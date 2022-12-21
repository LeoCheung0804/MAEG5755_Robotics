import numpy as np


class Trajectory_linear(object):
    def __init__(self, _init_x, _end_x, t_f):

        self.init_theta = _init_x
        self.end_theta = _end_x
        self.num_joints = len(_init_x)
        self.frequency = 50  # server update frequency
        self.t_f = t_f
        self.angle_min = [4, 0, -6]
        self.angle_max = [90, 180, 45]
        assert len(_init_x) == len(_end_x), 'DoF doesnt match! '
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

                angle_list[i].append(angles[i])
        return angle_list


theta_0 = [0, 50, 0]
theta_f = [40, 10, 1]
t_f = 3
if __name__ == '__main__':
    whole_traj = Trajectory_linear(theta_0, theta_f, t_f).get_whole_traj()
    return_str = 'angle;'
    for trajectory in whole_traj:
        return_str += ",".join([str(i) for i in trajectory]) + ";"
    print(return_str)
    with open('linear_trajectory.txt', 'w') as f:
        f.write(return_str)
