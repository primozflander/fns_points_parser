import numpy as np
from scipy.spatial.transform import Rotation as R


def translate_point_array(points, x, y, z):
    def translate_point(point):
        return (point[0] - x, point[1] - y, point[2] - z)
    return np.array(list(map(translate_point, points)))


def rotate_point(point, axis, angle):
    rot_mat = R.from_euler(axis, angle, degrees=True)
    return rot_mat.as_matrix().dot(point)


def rotate_point_array(array, axis, angle):
    rotated_array = [rotate_point(point, axis, angle) for point in array]
    return np.array(rotated_array, dtype=np.float32)


def convert_points_to_json_array(points):
    result = []
    scaling_factor = 1000
    [result.append({"w": 1, "x": coord[0]/scaling_factor, "y": coord[1]/scaling_factor, "z": coord[2]/scaling_factor}) for coord in points]
    return result
