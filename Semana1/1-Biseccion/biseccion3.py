import numpy as np
import math


def f(x):
    return math.exp(-x) - x


def bisection(f, a, b, tol):

    # check if a and b bound a root
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("The scalars a and b do not bound a root")

    # initialize variables
    c = (a + b) / 2
    fa = f(a)
    fb = f(b)
    fc = f(c)

    # initialize table
    print("a\t\tc\t\tb\t\tf(a)\t\tf(c)\t\tf(b)")
    print("-" * 89)

    # iterate until convergence or max iterations reached
    for i in range(1, 101):
        print(f"{a:.6f}\t{c:.6f}\t{b:.6f}\t{fa:.6f}\t{fc:.6f}\t{fb:.6f}")

        if np.abs(fc) < tol:
            return c

        if np.sign(fa) != np.sign(fc):
            b = c
            fb = fc
        else:
            a = c
            fa = fc

        c = (a + b) / 2
        fc = f(c)

    raise Exception("Bisection method failed to converge")


if __name__ == "__main__":

    a = 0
    b = 1
    tolerancia = 1e-3

    raiz_aproximada = bisection(f, a, b, tolerancia)
    print("La raíz aproximada es:", raiz_aproximada)
