import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Data
x = np.array([[1, 2], [1, 4], [1, 0],
              [10, 2], [10, 4], [10, 0]])

# Model
kmeans = KMeans(n_clusters=2)
kmeans.fit(x)

# Get labels
labels = kmeans.labels_

# Plot
plt.scatter(x[:, 0], x[:, 1], c=labels)
plt.title("K-Means Clustering")

plt.show()
