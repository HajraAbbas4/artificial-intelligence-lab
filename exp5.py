# ---------------- Experiment 5 ----------------
# Pandas and Matplotlib

import pandas as pd
import matplotlib.pyplot as plt


student_data = {
    "Name": ["Asha", "Ravi", "Neha", "Arjun", "Sara"],
    "Marks": [85, 78, 92, 74, 88],
}

df = pd.DataFrame(student_data)

print("\nExperiment 5: Pandas and Matplotlib")
print(df)
print("Average Marks:", df["Marks"].mean())

plt.figure()
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
