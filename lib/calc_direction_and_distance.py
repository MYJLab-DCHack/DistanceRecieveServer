import math
import numpy as np
class DirectionAndDistanceCalculator():
    def get_angle_to_rotate(self, cur_dir, cur_x, cur_y, des_x, des_y):
        current_loc = np.array([cur_x, cur_y])
        destination_loc = np.array([des_x, des_y])
        go_vec = destination_loc - current_loc
        x_axis =  np.array([1,0])
        x = np.inner(go_vec, x_axis)
        s = np.linalg.norm(go_vec)
        t = np.linalg.norm(x_axis)
        theta = np.arccos(x/(s*t))
        if ((current_loc[1] - destination_loc[1]) / ( current_loc[0] - destination_loc[0]) > 0):
            deg_theta = math.degrees(theta)
        else:
            deg_theta = 360 -  math.degrees(theta)
        print(deg_theta)
        if (deg_theta > cur_dir):
            return deg_theta - cur_dir
        else:
            return deg_theta + 360 - cur_dir

    def get_distance_to_go(self, cur_x, cur_y, des_x, des_y):
        current_loc = np.array([cur_x, cur_y])
        destination_loc = np.array([des_x, des_y])
        go_vec = destination_loc - current_loc
        return np.linalg.norm(go_vec)

print(get_angle_to_rotate(60, 0, 1, 1, 0))
print(get_distance_to_go(3, 2, 4, 3))