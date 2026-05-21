# ---------------- Experiment 4 ----------------
# Basic Libraries: Math, NumPy and SciPy

import math


print("\nExperiment 4: Math, NumPy and SciPy")

print("Using Math Library")
print("Square root of 25:", math.sqrt(25))
print("Factorial of 5:", math.factorial(5))
print("Power of 2 raised to 3:", math.pow(2, 3))

try:
    import numpy as np

    numbers = np.array([10, 20, 30, 40, 50])
    print("\nUsing NumPy Library")
    print("Array:", numbers)
    print("Mean:", np.mean(numbers))
    print("Standard Deviation:", np.std(numbers))
except ModuleNotFoundError:
    print("\nNumPy is not installed.")
    print("Install it using: pip install numpy")

try:
    from scipy import stats as scipy_stats

    scipy_numbers = [10, 20, 20, 30, 40, 50]
    mode_result = scipy_stats.mode(scipy_numbers, keepdims=True)
    print("\nUsing SciPy Library")
    print("Data:", scipy_numbers)
    print("Mode:", mode_result.mode[0])
except ModuleNotFoundError:
    print("\nSciPy is not installed.")
    print("Install it using: pip install scipy")
