import matplotlib.pyplot as plt
def draw_circle_bresenham(xc, yc, r):

    x = 0
    y = r
    d = 3 - 2 * r

    x_points = []
    y_points = []

    def plot_circle_points(xc, yc, x, y):

        x_points.extend([xc + x, xc - x, xc + x, xc - x, xc + y, xc - y, xc + y, xc - y])
        y_points.extend([yc + y, yc + y, yc - y, yc - y, yc + x, yc + x, yc - x, yc - x])

    plot_circle_points(xc, yc, x, y)

    while x < y:
        x += 1
        if d < 0:
            d = d + 4 * x + 6
        else:
            y -= 1
            d = d + 4 * (x - y) + 10
        plot_circle_points(xc, yc, x, y)

    plt.figure(figsize=(8, 8))
    plt.plot(x_points, y_points, 'ro', markersize=2)
    plt.title(f"Bresenham's Circle: Center=({xc},{yc}), Radius={r}")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.axis('equal')
    plt.show()

def main():
    draw_circle_bresenham(0, 0, 1000)

if __name__ == "__main__":
    main()