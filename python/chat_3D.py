import numpy as np
import matplotlib.pyplot as plt

# 立方体の頂点座標
vertices = np.array([[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1], [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]])

# 立方体の辺を表すインデックス
edges = np.array([[0, 1], [0, 2], [0, 4], [1, 3], [1, 5], [2, 3], [2, 6], [3, 7], [4, 5], [4, 6], [5, 7], [6, 7]])

# 回転行列を作成
theta = np.pi / 4 # 回転角
rx = np.array([[1, 0, 0], [0, np.cos(theta), -np.sin(theta)], [0, np.sin(theta), np.cos(theta)]])
ry = np.array([[np.cos(theta), 0, np.sin(theta)], [0, 1, 0], [-np.sin(theta), 0, np.cos(theta)]])
rz = np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])

# 立方体の頂点座標を回転
rotated_vertices = np.dot(np.dot(rx, ry), vertices.T).T

# 立方体を描画
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(edges)):
    ax.plot(rotated_vertices[edges[i], 0], rotated_vertices[edges[i], 1], rotated_vertices[edges[i], 2])

ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)
plt.show()
