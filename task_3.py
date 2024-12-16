import matplotlib.pyplot as plt

# Define the function and its derivative
def f(x):
    return x ** 2 - 3 * x + 2


def f_derivative(x):
    return 2 * x - 3


def newton_raphson(x0, accuracy=1e-6, max_iterations=100):
    iteration_data = []  # Here store the data for table and graph
    iteration = 0

    print(f"{'Iteration':<10}{'x_n':<15}{'Abs Error':<15}{'Rel Error':<15}")
    print("-" * 50)

    while iteration < max_iterations:
        # Evaluate the next iteration by formula (x_n+1 = x_n *]- f(x_n) / f'(x_n))
        x1 = x0 - f(x0) / f_derivative(x0)

        # Absolute Error
        abs_error = abs(x1 - x0)

        # Relative Error
        rel_error = abs_error / abs(x1) if x1 != 0 else float('inf')

        print(f"{iteration:<10}{x1:<15.6f}{abs_error:<15.6f}{rel_error:<15.6f}")

        # Store data for building graph
        iteration_data.append((iteration, abs_error))

        # Accuracy checking
        if abs_error < accuracy:
            print(f"\nThe root found: {x1:.6f} with accuracy {accuracy} for {iteration + 1} iterations.")
            return x1, iteration_data

        # Update values for the next iterations
        x0 = x1
        iteration += 1

    print("The maximum number of iterations ahs been exceeded")
    return None, iteration_data


# Graph building
def plot_convergence(data):
    iterations, errors = zip(*data)  # Разворачиваем данные
    plt.figure(figsize=(8, 6))
    plt.plot(iterations, errors, marker='o', label='Absolute Error')
    plt.yscale('log')  # Logarithmic scale
    plt.xlabel('Iteration Number')
    plt.ylabel('Absolute Error')
    plt.title('Newton-Raphson')
    plt.grid(True)
    plt.legend()
    plt.show()


def run():
    x0 = 2.5
    root, iteration_data = newton_raphson(x0)
    plot_convergence(iteration_data)
