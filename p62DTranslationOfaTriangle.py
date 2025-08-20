import numpy as np
import matplotlib.pyplot as plt
def draw_triangle(points, color='b', label=None):
    plt.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]], color=color)
    plt.plot([points[1][0], points[2][0]], [points[1][1], points[2][1]], color=color)
    plt.plot([points[2][0], points[0][0]], [points[2][1], points[0][1]], color=color, label=label)
def translate_points(points, tx, ty):
    translation_matrix = np.array([[1, 0, tx],
                                 [0, 1, ty],
                                 [0, 0, 1]])
    homogeneous_points = np.hstack((points, np.ones((3, 1))))
    translated_points = np.dot(homogeneous_points, translation_matrix.T)
    return translated_points[:, :2]
original_triangle = np.array([
    [1, 1],    
    [2, 3],    
    [3, 1]     
])
tx, ty = 2, 2 
translated_triangle = translate_points(original_triangle, tx, ty)
plt.figure(figsize=(10, 8))
plt.grid(True)
draw_triangle(original_triangle, 'b', 'Original Triangle')
draw_triangle(translated_triangle, 'r', 'Translated Triangle')
plt.title('2D Translation of a Triangle')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.axis('equal') 
plt.show()
