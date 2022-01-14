import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm
import numpy as np
import json

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(0, 0, 0, marker="x", c="red")

with open("targets/pf_zusatz_v3.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()
points = jsonObject["ModelData"]['points']

cnt = 1
for point in points:
    ax.scatter(point['x'], point['y'], point['z'], s=100)
    print(f"point_nr: {cnt} x: {point['x']}, y: {point['y']}, z: {point['z']}")
    cnt += 1

ax.set_title("Json points")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()


def show_3d():
    shape_points = []
    for point in points:
        shape_points.append([point['x'], point['y'], point['z']])
    shape_points = np.array(shape_points)
    xs = shape_points[:, 0]
    ys = shape_points[:, 1]
    zs = shape_points[:, 2]
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    surf = ax.plot_trisurf(xs, ys, zs, cmap=cm.jet, linewidth=0)
    fig.colorbar(surf)
    ax.xaxis.set_major_locator(MaxNLocator(5))
    ax.yaxis.set_major_locator(MaxNLocator(6))
    ax.zaxis.set_major_locator(MaxNLocator(5))
    fig.tight_layout()
    plt.show()  # or:
    # fig.savefig('3D.png')

#show_3d()