import numpy as np
import matplotlib.pyplot as plt
def draw_triangle(points, color='b', label=None):
    plt.plot([points[0][0], points[1][0]], [points[0][1], points[1][1]], color=color)
    plt.plot([points[1][0], points[2][0]], [points[1][1], points[2][1]], color=color)
    plt.plot([points[2][0], points[0][0]], [points[2][1], points[0][1]], color=color, label=label)
def shear_points(points, shx=0, shy=0):
    shear_matrix = np.array([[1, shx, 0],
                            [shy, 1, 0],
                            [0, 0, 1]])
    homogeneous_points = np.hstack((points, np.ones((3, 1))))
    sheared_points = np.dot(homogeneous_points, shear_matrix.T)
    return sheared_points[:, :2]
original_triangle = np.array([
    [1, 1],  
    [2, 3],   
    [3, 1]    
])
shx = 0.5 
shy = 0.3  
sheared_triangle_x = shear_points(original_triangle, shx=shx, shy=0)
sheared_triangle_y = shear_points(original_triangle, shx=0, shy=shy) 
plt.figure(figsize=(12, 10))
plt.grid(True)
draw_triangle(original_triangle, 'b', f'Original Triangle')
draw_triangle(sheared_triangle_x, 'r', f'Sheared in X-direction (shx={shx})')
draw_triangle(sheared_triangle_y, 'g', f'Sheared in Y-direction (shy={shy})')
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.title('2D Shearing of a Triangle')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.axis('equal')  
plt.show()