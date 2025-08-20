import numpy as np
import matplotlib.pyplot as plt
def draw_line(points, color='b', label=None):
    plt.plot([points[0][0], points[1][0]],
             [points[0][1], points[1][1]],
             color=color,
             label=label)
def rotate_points(points, angle_degrees):
    angle_rad = np.radians(angle_degrees)
    rotation_matrix = np.array([[np.cos(angle_rad), -np.sin(angle_rad), 0],
                               [np.sin(angle_rad), np.cos(angle_rad), 0],
                               [0, 0, 1]])
    homogeneous_points = np.hstack((points, np.ones((2, 1))))
    rotated_points = np.dot(homogeneous_points, rotation_matrix.T)
    return rotated_points[:, :2]
original_line = np.array([
    [0, 0],   
    [3, 0]    
])
angles = [0, 45, 90, 135, 180] 
plt.figure(figsize=(10, 10))
plt.grid(True)
colors = ['b', 'r', 'g', 'm', 'c']
for angle, color in zip(angles, colors):
    rotated_line = rotate_points(original_line, angle)
    draw_line(rotated_line, color=color, label=f'Rotation {angle}°')
plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
plt.title('2D Rotation of a Line')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.axis('equal')
plt.show()
def animate_rotation():
    plt.figure(figsize=(10, 10))
    for angle in range(0, 361, 5): 
        plt.clf() 
        plt.grid(True)
        rotated_line = rotate_points(original_line, angle)
        draw_line(rotated_line, color='r', label=f'Rotation {angle}°')
        plt.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        plt.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        plt.title('2D Rotation of a Line (Animation)')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.legend()
        plt.axis('equal')
        plt.xlim(-4, 4)
        plt.ylim(-4, 4)
        plt.pause(0.1) 
    plt.show()