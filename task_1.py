import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root_scalar

# Define the function
def f(x):
    return x**3 - 2*x**2 - 5


# Create the diapason of x
x = np.linspace(1, 4, 1000)
y = f(x)

# Set approximate root and show it on the graph
approximate_root = 2.69
x1 = np.array(approximate_root)
y1 = np.array(0)

# Find the value of approximate root using formula
approximate_root_value = f(approximate_root)


# Find the exact root
solution = root_scalar(f, bracket=[2, 3], method="bisect")
exact_root = solution.root

# Find the absolut error
absolute_error = abs(approximate_root - exact_root)

# Build the graph
def run():
    plt.plot(x, y, label='f(x) = x^3 - 2x^2 - 5')
    plt.axhline(0, color='red', linestyle='--', label='y = 0')  # Line y = 0
    plt.plot(
        x1, y1,
             color="red",
             linestyle="dashed",
             linewidth=2, marker="o",
             markersize=5,
             markerfacecolor="red",
             markeredgecolor="red",
             label="approximate root"
    )
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph of function')
    plt.legend()
    plt.grid()
    plt.show()

