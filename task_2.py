import numpy as np

# Define the function
def f(x):
    return np.e**x - 2*x - 3


def bisection_method(first_point, second_point, accuracy=1e-6, iteration=0):
    # The check of conditions
    if f(first_point) * f(second_point) >= 0:
        raise ValueError("The function must have the opposite signs on at the end of the interval")

    # Middle point of the interval
    middle_point = (first_point + second_point) / 2

    # Print iteration
    print(f"Iteration {iteration}: Root = {middle_point:.6f}")

    # Accuracy checking and iteration limit checking
    if abs(f(middle_point)) < accuracy:
        print(f"\nRoot found: {middle_point:.6f} with accuracy {accuracy}. Iterations: {iteration}")
        return middle_point

    if f(first_point) * f(middle_point) < 0:
        return bisection_method(first_point, middle_point, accuracy, iteration + 1)
    else:
        return bisection_method(middle_point, second_point, accuracy, iteration + 1)


def secant_method(x0, x1, accuracy=1e-6, max_iterations=100):
    def secant_formula():
        return x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)

    iteration = 0
    print('Iteration \t\t\t Root')

    while iteration < max_iterations:
        # Evaluate the function values of points
        f_x0, f_x1 = f(x0), f(x1)

        # Zero division checking
        if abs(f_x1 - f_x0) < 1e-12:
            print("Method is not working. Division on zero")
            return None

        # Save the value of formula in x2 variable
        x2 = secant_formula()

        print(f"{iteration} \t\t\t {x1:.6f}")

        # Accuracy checking
        if abs(f(x2)) < accuracy:
            print(f"\nRoot is found: {x2:.6f} with accuracy {accuracy}. Iterations: {iteration + 1}")
            return x2, iteration + 1

        # Update points for the next iteration
        x0, x1 = x1, x2
        iteration += 1

    print("The maximum number of iterations ahs been exceeded")
    return None


def count_relative_error():
    exact_root = secant_method(0, 2, accuracy=1e-15)[0]
    print("This is exact root\n")
    approx_root = secant_method(0, 2)[0]
    print("This is approximate root")
    return abs(exact_root - approx_root) / abs(exact_root)


def run():
    print("\n Bisection method for interval [0, 2]")
    print("-"*50)
    bisection_method(0, 2)
    print("-"*50)
    print(f"\n{"-"*50}\n Secant method for interval [0, 2]")
    secant_method(0, 2)
    print("-"*50)
    print(f"\n\n Relative Error: {count_relative_error()}")
    print("-"*50)
    print("\nSummarization: The secant method is more effective rather than bisection method. For secant method 5 iterations < for bisection method 18 iterations")
