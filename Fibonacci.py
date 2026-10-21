import math
def fibonacci_method(func, eps, interval):
    a, b = interval[0], interval[1]
    Fibonacci = [0, 1, 1, 2]
    while Fibonacci[-1] < (b-a)/eps:
        Fibonacci.append(Fibonacci[-1] + Fibonacci[-2])
    N = len(Fibonacci) - 3

    a_trial, b_trial = (a + (b-a) * Fibonacci[-3]/Fibonacci[-1],
                        b - (b-a) * Fibonacci[-3]/Fibonacci[-1])
    f_a, f_b = func(a_trial), func(b_trial)
    for i in range(N, 1, -1):
        if f_a < f_b:
            b = b_trial
            b_trial, f_b = a_trial, f_a
            a_trial = a + (b - a) * Fibonacci[i - 1] / Fibonacci[i + 1]
            f_a = func(a_trial)
        else:
            a = a_trial
            a_trial, f_a = b_trial, f_b
            b_trial = b - (b - a) * Fibonacci[i - 1] / Fibonacci[i + 1]
            f_b = func(b_trial)

    x = (a + b) / 2
    return x, func(x), N
def f_1(x):
    return (x-1.7)**4+(x-1.7)**2+0.5
def f_2(x):
    return math.exp(0.5*(x-2))+(x-2)**6+0.1*(x-2)**2
# print(fibonacci_method(f_1, 10**-5, [0, 4]))
# print(fibonacci_method(f_2, 10**-6, [-1, 5]))