import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**2 - 2*x

# False Position Method
def false_position(a, b, accuracy=1e-6, max_iter=50):
    iterations = 0
    abs_errors = []
    root = None

    while iterations < max_iter:
        # Check for division by zero
        if f(b) - f(a) == 0:
            print("Division by zero encountered. Exiting.")
            break

        # New point made by false position method
        x_new = (a * f(b) - b * f(a)) / (f(b) - f(a))
        abs_error = abs(f(x_new))

        abs_errors.append(abs_error)

        # Stop checking
        if abs_error < accuracy:
            root = x_new
            break

        # Update the edges of interval
        if f(a) * f(x_new) < 0:
            b = x_new
        elif f(b) * f(x_new) < 0:
            a = x_new
        else:
            print("Root not bracketed properly. Exiting.")
            break

        iterations += 1

    return root, abs_errors, iterations


def run():
    a, b = 1, 3  # Adjust interval to avoid f(b) = 0 at the start
    root, abs_errors, total_iterations = false_position(a, b)

    if abs_errors:
        # Building the plot
        plt.plot(range(1, len(abs_errors) + 1), abs_errors, marker='o')
        plt.xlabel('Iteration')
        plt.ylabel('Absolute Error')
        plt.title('Absolute Error vs Iteration (False Position Method)')
        plt.grid()
        plt.show()

    print(f"Root found: {root}")
    print(f"Total Iterations: {total_iterations}")

