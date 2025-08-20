import matplotlib.pyplot as plt
import numpy as np
def create_triangle():
    triangle = np.array([
        [1, 3],    
        [2, 5],    
        [3, 3]   
    ])
    return triangle
def scale_triangle(triangle, sx, sy):
    scaling_matrix = np.array([
        [sx, 0],
        [0, sy]
    ])
    scaled_triangle = triangle @ scaling_matrix.T
    return scaled_triangle
def demonstrate_scaling():
    original_triangle = create_triangle()
    sx, sy = 1.5, 1.5
    scaled_triangle = scale_triangle(original_triangle, sx, sy)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle('2D Triangle Scaling Demonstration', fontsize=16, fontweight='bold')
    orig_plot = np.vstack([original_triangle, original_triangle[0]])  
    ax1.plot(orig_plot[:, 0], orig_plot[:, 1], 'o-', color='blue',
            linewidth=2, markersize=8, label='Original')
    ax1.set_title('Original Triangle')
    ax1.grid(True, alpha=0.3)
    ax1.set_xlabel('X coordinate')
    ax1.set_ylabel('Y coordinate')
    ax1.legend()
    ax1.axis('equal')
    scaled_plot = np.vstack([scaled_triangle, scaled_triangle[0]])
    ax2.plot(orig_plot[:, 0], orig_plot[:, 1], 'o-', color='blue',
            linewidth=2, markersize=6, alpha=0.5, label='Original')
    ax2.plot(scaled_plot[:, 0], scaled_plot[:, 1], 'o-', color='red',
            linewidth=2, markersize=8, label=f'Scaled (sx={sx}, sy={sy})')
    ax2.set_title(f'Scaled Triangle (sx={sx}, sy={sy})')
    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('X coordinate')
    ax2.set_ylabel('Y coordinate')
    ax2.legend()
    ax2.axis('equal')
    plt.tight_layout()
    plt.show()
if __name__ == "__main__":
    demonstrate_scaling()