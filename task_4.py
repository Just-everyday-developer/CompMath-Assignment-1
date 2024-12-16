import numpy as np


# Define the function
def f(x):
    return x**3 + x**2 + x + 1


# Muller's Method
def mullers_method(start1, start2, start3, tolerance=1e-6, max_iterations=100):
    for _ in range(max_iterations):
        # Evaluate function values of initial approximations
        f0, f1, f2 = f(start1), f(start2), f(start3)

        # Differences between the points
        diff1, diff2 = start2 - start1, start3 - start2
        if diff1 == 0 or diff2 == 0:
            raise ValueError("Division by zero encountered in step sizes.")

        # Use Muller Method
        delta1 = (f1 - f0) / diff1
        delta2 = (f2 - f1) / diff2
        a = (delta2 - delta1) / (diff2 + diff1)
        b = a * diff2 + delta2
        c = f2

        # Formula for Discriminant
        discriminant = b ** 2 - 4 * a * c

        if discriminant >= 0:
            sqrt_discriminant = np.sqrt(discriminant)
        else:
            sqrt_discriminant = np.sqrt(complex(discriminant))

        if b + sqrt_discriminant != 0:
            root1 = start3 + (-2 * c) / (b + sqrt_discriminant)
        else:
            root1 = start3

        if b - sqrt_discriminant != 0:
            root2 = start3 + (-2 * c) / (b - sqrt_discriminant)
        else:
            root2 = start3

        x3 = root1 if abs(root1 - start3) < abs(root2 - start3) else root2

        if abs(x3 - start3) < tolerance:
            return x3, f(x3), abs(f(x3))

        start1, start2, start3 = start2, start3, x3

    raise ValueError("Muller's method did not converge within the maximum number of iterations.")


def run():
    # Initial approximations
    x0, x1, x2 = -1, 0, 1
    try:
        root, f_val_at_root, absolute_error = mullers_method(x0, x1, x2)

        # Output the results
        print(f"Root: {root}")
        print(f"Value of f(root): {f_val_at_root}")
        print(f"Absolute error: {absolute_error}")
    except ValueError as e:
        print(f"Error: {e}")