import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm
import numpy as np
import json


with open("targets/zusatz_v2.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

points = jsonObject["ModelData"]['points']

shape_points = []
for point in points:
    shape_points.append([point['x'], point['y'], point['z']])
shape_points = np.array(shape_points)

#[DATA.append([point['x'], point['y'], point['z']]) for point in points]

'''''
DATA = np.array([
    [0.021280129, -0.015578032, -0.01693803],
    [0.007495987, 0.0006812364, -0.017220557],
    [-0.005111861, 0.003358528, -0.0115816],
    [-0.017134089, -0.009314328, -0.014082134],
    [0.016895445, 0.006702006, -0.0036054254],
    [0.0059403786, 0.015983045, 0.005826056],
    [-0.0056256074, 0.016063064, 0.015914142],
    [-0.01724923, -0.0049419254, 0.0036581159],
    [0.025852293, 0.012237415, 0.015055239],
    [-0.014157492, -0.0010131896, 0.02321291],
    [-0.018185955, -0.0241777, -0.0002385974],
])
print(type(DATA))
'''''

Xs = shape_points[:, 0]
Ys = shape_points[:, 1]
Zs = shape_points[:, 2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_trisurf(Xs, Ys, Zs, cmap=cm.jet, linewidth=0)
fig.colorbar(surf)

ax.xaxis.set_major_locator(MaxNLocator(5))
ax.yaxis.set_major_locator(MaxNLocator(6))
ax.zaxis.set_major_locator(MaxNLocator(5))

fig.tight_layout()

plt.show()  # or:
# fig.savefig('3D.png')