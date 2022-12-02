def generate_object_trajectory():
    # generate angle lists
    position_x_list = [i for i in range(5)]
    position_y_list = [i for i in range(5)]
    position_z_list = [i for i in range(5)]
    rotation_x_list = [i for i in range(5)]
    rotation_y_list = [i for i in range(5)]
    rotation_z_list = [i for i in range(5)]

    return [position_x_list, position_y_list, position_z_list, rotation_x_list, rotation_y_list, rotation_z_list]

trajectories = generate_object_trajectory()
return_str = ''
for trajectory in trajectories:
    return_str += ",".join([str(i) for i in trajectory]) + ";"
print(return_str)
with open('object_trajectory.txt', 'w') as f:
    f.write(return_str)
