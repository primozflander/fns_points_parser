import json
import matplotlib.pyplot as plt
import numpy as np
import helpers as hp


# scaling_factor = 1000
# fig = plt.figure(figsize=(10, 10))
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(0, 0, 0, marker="x", c="red")
#
#
# with open("targets/pf_zusatz_v2.json") as jsonFile:
#     jsonObject = json.load(jsonFile)
#     jsonFile.close()
# points_zv2 = jsonObject["ModelData"]['points']
#
# with open("targets/pf_zusatz_v3.json") as jsonFile:
#     jsonObject = json.load(jsonFile)
#     jsonFile.close()
# points_zv3 = jsonObject["ModelData"]['points']
#
#
# point_array = []
# #[point_array.append([point['x'], point['y'], point['z']]) for point in points]
# for point in points_zv2:
#     if point['x'] < -0.15:
#         point_array.append([point['x'], point['y'], point['z']])
# for point in points_zv3:
#     if point['x'] > -0.15:
#         point_array.append([point['x'], point['y'], point['z']])
# point_array = np.array(point_array)
#
#
# # rotation
# #point_array = hp.rotate_point_array(point_array, "x", 90)
# # translation
# #point_array = hp.translate_point_array(point_array, -0.075, 0, 0)
#
#
# count = 0
# f = open("generated_points_zusatz_v2_v3.txt", "w")
# for point in point_array:
#     f.write(f"{point[0] * scaling_factor}\t{point[1] * scaling_factor}\t{point[2] * scaling_factor}\n")
#     ax.scatter(point[0], point[1], point[2], s=100)
#     # print(f"x: {point['x']}, y: {point['y']}, z: {point['z']}")
#     count += 1
# print(f"Number of points: {count}")
# f.close()
# ax.set_title("Json points")
# ax.set_xlabel("x")
# ax.set_ylabel("y")
# ax.set_zlabel("z")
# plt.show()

scaling_factor = 1000
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(0, 0, 0, marker="x", c="red")


with open("targets/pf_zusatz_v2.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
points_zv2 = jsonObject["ModelData"]['points']

with open("targets/pf_zusatz_v3.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
points_zv3 = jsonObject["ModelData"]['points']


point_array = []
#[point_array.append([point['x'], point['y'], point['z']]) for point in points]
# for point in points_zv2:
#     if point['x'] < -0.15:
#         point_array.append([point['x'], point['y'], point['z']])
for point in points_zv3:
    if point['x'] > -0.15:
        point_array.append([point['x'], point['y'], point['z']])
point_array = np.array(point_array)


# # rotation
# point_array = hp.rotate_point_array(point_array, "y", 180)
# # translation
# point_array = hp.translate_point_array(point_array, 0.235, 0, 0)

# rotation
point_array = hp.rotate_point_array(point_array, "y", -90)
# translation
point_array = hp.translate_point_array(point_array, 0, 0, -0.135)
point_array = hp.rotate_point_array(point_array, "z", 25)


count = 0
f = open("generated_points", "w")
for point in point_array:
    f.write(f"{point[0] * scaling_factor}\t{point[1] * scaling_factor}\t{point[2] * scaling_factor}\n")
    ax.scatter(point[0], point[1], point[2], s=100)
    # print(f"x: {point['x']}, y: {point['y']}, z: {point['z']}")
    count += 1
print(f"Number of points: {count}")
f.close()
ax.set_title("Json points")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()

