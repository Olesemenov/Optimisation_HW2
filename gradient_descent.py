import numpy as np

from Fibonacci import fibonacci_method


def gradient(f, x, h=1e-6):
    grad = np.zeros_like(x)
    for _ in range(x.size):
        e = np.zeros_like(x)
        e[_] = h
        grad[_] = (f(x+e) - f(x))/h
    return grad

def gradient_descent(f, x_start, step = None, max_iter=10**6, eps = 1e-4, epsilon=1e-4):
    x = np.array(x_start, dtype=float)
    steps = [x.copy()]
    for i in range(max_iter):
        grad = gradient(f, x)
        if np.linalg.norm(grad) < epsilon:
            break

        if step is None:
            def phi(alpha, x=x, grad=grad):
                return f(x-alpha*grad)

            alpha_max = 1.0
            while alpha_max < 1e4 and phi(alpha_max) < phi(alpha_max/2):
                alpha_max *= 2
            alpha = fibonacci_method(phi, eps, [0, alpha_max])[0]
        else:
            alpha = step

        x = x - alpha*grad
        steps.append(x.copy())
        if i>=max_iter:
            return "max_iter reached"

    return x, f(x), i, steps
def quadratic(a, b):
    def f(x):
        return a * x[0]**2 + b * x[1]**2
    return f
def rosenbrock(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

x, fx, iters, steps = gradient_descent(rosenbrock, [2.0, 2.5])
print(x, fx, iters, np.linalg.norm(gradient(rosenbrock, x)))
