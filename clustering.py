import matplotlib.pyplot as plt
import seaborn as sns; sns.set()  # for plot styling
import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs

# https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html
X, y_true = make_blobs(n_samples=300, n_features=400, centers=4,
                       cluster_std=0.60, random_state=0)

print X
plt.scatter(X[:, 0], X[:, 1], s=50);

kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

print y_kmeans