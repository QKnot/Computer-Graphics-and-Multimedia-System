import matplotlib.pyplot as plt
def draw_circle_midpoint(xc, yc, r):
    points = []
    x = 0
    y = r
    p = 1 - r 
    add_circle_points(xc, yc, x, y, points)
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        add_circle_points(xc, yc, x, y, points)
    return points
def add_circle_points(xc, yc, x, y, points):
    """
    Add points for all eight octants of the circle
    """
    points.extend([
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)
    ])

def plot_circle(points, title):
    x_values, y_values = zip(*points)
    plt.plot(x_values, y_values, 'bo')  # 'bo' for blue dots
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.axis('equal')  
    plt.show()
def main():
    circle_points = draw_circle_midpoint(0, 0, 5)
    plot_circle(circle_points, 'Midpoint Circle Drawing Algorithm')
if __name__ == "__main__":
    main()