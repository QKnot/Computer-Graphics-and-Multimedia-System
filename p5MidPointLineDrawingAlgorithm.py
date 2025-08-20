import matplotlib.pyplot as plt
def draw_line_midpoint(x1, y1, x2, y2):
    points = []
    dx = x2 - x1
    dy = y2 - y1
    x, y = x1, y1
    points.append((x, y))
    d = dy - (dx / 2)
    while x < x2:
        x += 1
        if d < 0:
            d = d + dy
        else:
            y += 1
            d = d + (dy - dx)
        points.append((x, y))
    return points
def plot_line(points, title):
    x_values, y_values = zip(*points)
    plt.plot(x_values, y_values, marker='o')
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()
x1, y1 = 3, 5
x2, y2 = 6, 7
midpoint_points = draw_line_midpoint(x1, y1, x2, y2)
plot_line(midpoint_points, "Midpoint Line Drawing")