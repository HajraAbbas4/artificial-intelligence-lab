# ---------------- Experiment 3 ----------------
# Mean, Median, Mode, Variance and Standard Deviation

import statistics as stats


data = [12, 15, 13, 14, 16, 12, 15, 17, 14, 13]

print("\nExperiment 3: Statistical Measures")
print("Data:", data)
print("Mean:", stats.mean(data))
print("Median:", stats.median(data))
print("Mode:", stats.mode(data))
print("Variance:", stats.variance(data))
print("Standard Deviation:", stats.stdev(data))
