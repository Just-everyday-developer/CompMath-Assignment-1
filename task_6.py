import matplotlib.pyplot as plt

# Iterative function g(x)
def g(x):
    return (x**2 + 5) / 6

# Iterative method
def fixed_point_iteration(x0, true_root, max_iter=10):
    x_values = [x0]  # Storing x values
    abs_errors = []  # Storing absolute errors

    for i in range(1, max_iter + 1):
        x_new = g(x_values[-1])  # Compute the next approximation
        abs_error = abs(x_new - true_root)  # Absolute error
        x_values.append(x_new)
        abs_errors.append(abs_error)

        print(f"Iteration {i}: x = {x_new:.6f}, Absolute Error = {abs_error:.6f}")

    return x_values, abs_errors

def run():
    true_root = 5.0  # Exact root
    x0 = 0.5         # Initial value

    x_values, abs_errors = fixed_point_iteration(x0, true_root)

    # Plotting the graph of absolute errors
    plt.plot(range(1, len(abs_errors) + 1), abs_errors, marker='o')
    plt.xlabel('Iteration')
    plt.ylabel('Absolute Error')
    plt.title('Absolute Error vs Iteration (Iteration Method)')
    plt.grid()
    plt.show()

