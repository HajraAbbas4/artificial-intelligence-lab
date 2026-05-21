# Experiment 6
# Normal and Poisson Distribution using Python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, norm

# Poisson Distribution
poisson_data = np.array([12, 15, 13, 14, 16, 12, 15, 17, 14, 13])

lam = np.mean(poisson_data)
print("Poisson Distribution")
print("Lambda:", lam)

x_poisson = np.arange(0, max(poisson_data) + 5)
y_poisson = poisson.pmf(x_poisson, lam)

plt.figure()
plt.bar(x_poisson, y_poisson)
plt.title("Poisson Distribution - Aadhaar Submissions per Hour")
plt.xlabel("Number of Submissions")
plt.ylabel("Probability")
plt.show()

# Normal Distribution
normal_data = np.array([8.5, 9.2, 8.8, 9.5, 8.9, 9.1, 9.3, 8.7, 9.0, 9.4])

mu = np.mean(normal_data)
sigma = np.std(normal_data)

print("\nNormal Distribution")
print("Mean:", mu)
print("Standard Deviation:", sigma)

density = norm.pdf(9.0, mu, sigma)
print("Density at x = 9.0:", density)

x_normal = np.linspace(min(normal_data), max(normal_data), 100)
y_normal = norm.pdf(x_normal, mu, sigma)

plt.figure()
plt.hist(normal_data, bins=5, density=True)
plt.plot(x_normal, y_normal)
plt.title("Normal Distribution - Car Sales")
plt.xlabel("Sales Value in Lakhs")
plt.ylabel("Density")
plt.show()
