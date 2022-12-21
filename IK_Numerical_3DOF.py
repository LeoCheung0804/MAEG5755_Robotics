import numpy as np
import FK_2

def solve_ik(T_desired, T_current, joint_angles, step_size=0.1, tolerance=1e-6):

    while True:

        T_error = np.matmul(T_desired, np.linalg.inv(T_current))

        joint_velocities = np.zeros(3)
        for i in range(3):
            joint_velocities[i] = T_error[i, 3]

        joint_angles += step_size * joint_velocities

        T_current =FK_2.FK(joint_angles)

        if np.abs(T_error[:3, 3]).max() < tolerance:
            break

    return joint_angles

if __name__ == '__main__':
    T_desired =  [23.77 , 0 , 11]
    T_current =  [0 , 0 , 0]
    joint_angles = 3
    solve_ik = solve_ik(T_desired, T_current, joint_angles)