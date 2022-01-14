import json
import matplotlib.pyplot as plt
import numpy as np
import helpers as hp


scaling_factor = 1000
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
#ax.scatter(0, 0, 0, marker="x", c="red")

with open("targets/pf_umgebung_p2_sw.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
points = jsonObject["ModelData"]['points']


point_array = []
[point_array.append([point['x'], point['y'], point['z']]) for point in points]
point_array = np.array(point_array)

# rotation
point_array = hp.rotate_point_array(point_array, "x", 90)
# translation
point_array = hp.translate_point_array(point_array, 0.0005, -0.0027, -0.0158)

count = 0
f = open("C:\FH_Projects\Fronius\SolidWorks\points.txt", "w")
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





