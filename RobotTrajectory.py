def generate_robot_trajectory():
    # generate angle lists
    angle_0_list = list(reversed([i for i in range(0, 5)]))
    angle_1_list = [i for i in range(5)]
    angle_2_list = [i for i in range(5)]
    # add 'fire' to toggle the end effector
    angle_0_list.append('fire')
    angle_1_list.append('fire')
    angle_2_list.append('fire')
    angle_0_list += reversed(angle_0_list)
    angle_1_list += reversed(angle_1_list)
    angle_2_list += reversed(angle_2_list)

    return [angle_0_list, angle_1_list, angle_2_list]

trajectories = generate_robot_trajectory()
return_str = 'angle;'
for trajectory in trajectories:
    return_str += ",".join([str(i) for i in trajectory]) + ";"
print(return_str)
with open('robot_trajectory.txt', 'w') as f:
    f.write(return_str)
