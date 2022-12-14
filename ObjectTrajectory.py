
import numpy as np

def generate_object_trajectory(px,py,pz,rx,ry,rz):
    # generate angle lists
    position_x_list = [px]
    position_y_list = [py]
    position_z_list = [pz]
    rotation_x_list = [rx]
    rotation_y_list = [ry]
    rotation_z_list = [rz]

    return [position_x_list, position_y_list, position_z_list, rotation_x_list, rotation_y_list, rotation_z_list]

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

obj_x_0 = [-30]
obj_x_f = [10]
obj_y_0 = [0]
obj_y_f = [0]
obj_z_0 = [0]
obj_z_f = [-40]
obj_r_0 = [0,0,0]
obj_r_f = [0,0,0]
t_f = 3

if __name__ == '__main__':
    x_traj = Trajectory_linear(obj_x_0, obj_x_f, t_f).get_whole_traj()
    y_traj = Trajectory_linear(obj_y_0, obj_y_f, t_f).get_whole_traj()
    z_traj = Trajectory_linear(obj_z_0, obj_z_f, t_f).get_whole_traj()
    px = x_traj
    py = y_traj
    pz = z_traj
    rx = 0
    ry = 0
    rz = 0
    return_str = ''
    obj_trajectory = generate_object_trajectory(px, py, pz, rx, ry, rz)
    for trajectory in obj_trajectory:
        return_str += ",".join([str(i) for i in trajectory]) + ";"
    print(return_str)
    with open('object_trajectory.txt', 'w') as f:
        f.write(return_str)
