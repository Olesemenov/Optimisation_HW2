import numpy as np

from Fibonacci import fibonacci_method


def gradient(f, x, h=1e-6):
    grad = np.zeros_like(x)
    for _ in range(x.size):
        e = np.zeros_like(x)
        e[_] = h
        grad[_] = (f(x+e) - f(x))/h
    return grad

def with_counter(f):
    count = 0
    def counted(x):
        nonlocal count
        count += 1
        return f(x)

    def get_count():
        return count

    return counted, get_count

def gradient_descent(f, x_start, step = None, max_iter=10**6, eps = 1e-4, epsilon=1e-4):
    x = np.array(x_start, dtype=float)
    steps = [x.copy()]
    for iteration in range(max_iter):
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
    else:
        return "max_iter reached"
    gradient_norm = np.linalg.norm(gradient(f, x))
    return x, f(x), iteration, steps, gradient_norm
def quadratic(a, b):
    def f(x):
        return a * x[0]**2 + b * x[1]**2
    return f
def rosenbrock(x):
    return (1 - x[0])**2 + 100 * (x[1] - x[0]**2)**2

f, get_count = with_counter(rosenbrock)
result = gradient_descent(f, [5.0, -5.0])

if result == "max_iter reached":
    print("max_iter reached")
else:
    x, fx, iters, steps, grad = result
    print(x, fx, iters, grad, get_count())
