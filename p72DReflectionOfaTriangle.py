import numpy as np
import matplotlib.pyplot as plt
def draw_triangle(points, color='b', label=None):
    plt.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]], color=color)
    plt.plot([points[1][0], points[2][0]], [points[1][1], points[2][1]], color=color)
    plt.plot([points[2][0], points[0][0]], [points[2][1], points[0][1]], color=color, label=label)
def reflect_points(points, axis='x'):
    if axis.lower() == 'x':
        reflection_matrix = np.array([[1, 0, 0],
                                    [0, -1, 0],
                                    [0, 0, 1]]) 
    else:
        reflection_matrix = np.array([[-1, 0, 0],
                                    [0, 1, 0],
                                    [0, 0, 1]]) 
    homogeneous_points = np.hstack((points, np.ones((3, 1))))
    reflected_points = np.dot(homogeneous_points, reflection_matrix.T)
    return reflected_points[:, :2]
original_triangle = np.array([
    [1, 1],  
    [2, 3],    
    [3, 1]     
])
reflected_triangle_x = reflect_points(original_triangle, 'x')
reflected_triangle_y = reflect_points(original_triangle, 'y')
plt.figure(figsize=(12, 10))
plt.grid(True)
draw_triangle(original_triangle, 'b', 'Original Triangle')
draw_triangle(reflected_triangle_x, 'r', 'Reflected about X-axis')
draw_triangle(reflected_triangle_y, 'g', 'Reflected about Y-axis')
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.title('2D Reflection of a Triangle')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.axis('equal')  
plt.show()