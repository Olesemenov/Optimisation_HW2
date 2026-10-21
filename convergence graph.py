import matplotlib.pyplot as plt
from gradient_descent import gradient_descent, quadratic, rosenbrock
def plot(f, x_start, max_iters = 15000, title = ""):

    steps = gradient_descent(f, x_start, max_iter = max_iters)[3]

    values = [f(x) for x in steps]

    plt.plot(values, "o", markersize=3)
    plt.xlabel('iteration')
    plt.ylabel('f(x)')
    plt.yscale('log')
    plt.title(title)
    plt.grid(True)
    plt.show()

plot(rosenbrock, [5.0, -5.0], 10**6, "rosenbrock")
