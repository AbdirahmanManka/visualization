import numpy as np
import matplotlib.pyplot as plt

# Generate x values from 0 to 2*pi with 0.1 intervals
x = np.arange(0, 2*np.pi, 0.1)

# Plot sin(x) in blue solid line
plt.plot(x, np.sin(x), label='sin(x)', color='blue', linestyle='-')

# Plot cos(x) in red dashed line
plt.plot(x, np.cos(x), label='cos(x)', color='red', linestyle='--')

# Plot -sin(x) in green dashed line
plt.plot(x, -np.sin(x), label='-sin(x)', color='green', linestyle='--')

# Plot tan(x) in magenta dotted line
plt.plot(x, np.tan(x), label='tan(x)', color='magenta', linestyle=':')

# Add grid
plt.grid(True)

# Add title and labels
plt.title('Trigonometric Functions')
plt.xlabel('x')
plt.ylabel('y')

# Add legend
plt.legend()

# Display the plot
plt.show()
