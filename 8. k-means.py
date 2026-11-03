import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


# K-Means Clustering class
class KMeansCustom:

    def __init__(self, n_clusters, max_iterations=100):
        self.n_clusters = n_clusters
        self.max_iterations = max_iterations

    # Step 1: Initialize random centroids
    def initialize_centroids(self, data):
        random_indices = np.random.choice(
            data.shape[0],
            size=self.n_clusters,
            replace=False
        )

        centroids = data[random_indices]

        return centroids

    # Step 2: Assign each data point to the nearest centroid
    def assign_to_clusters(self, data, centroids):

        clusters = []

        for point in data:
            distances = []

            for centroid in centroids:
                # Euclidean distance
                distance = np.sqrt(
                    np.sum((point - centroid) ** 2)
                )

                distances.append(distance)

            # Find the nearest centroid
            closest = np.argmin(distances)

            clusters.append(closest)

        return np.array(clusters)

    # Step 3: Calculate new centroids
    def update_centroids(self, data, clusters):

        new_centroids = []

        for i in range(self.n_clusters):

            # Get all points belonging to cluster i
            cluster_points = data[clusters == i]

            if len(cluster_points) > 0:

                # Calculate mean of all points in the cluster
                centroid = np.mean(cluster_points, axis=0)

            else:
                # If cluster is empty, keep the first data point
                centroid = data[0]

            new_centroids.append(centroid)

        return np.array(new_centroids)

    # Step 4: Run the K-Means algorithm
    def fit(self, data):

        # Initialize centroids
        centroids = self.initialize_centroids(data)

        for _ in range(self.max_iterations):

            # Assign points to nearest centroid
            clusters = self.assign_to_clusters(data, centroids)

            # Calculate new centroids
            new_centroids = self.update_centroids(data, clusters)

            # Stop if centroids do not change
            if np.allclose(centroids, new_centroids):
                break

            # Update centroids
            centroids = new_centroids

        self.centroids = centroids
        self.labels = clusters

        return centroids, clusters


# --------------------------------------------------
# Main Program
# --------------------------------------------------

# Load Iris dataset
iris = load_iris()

# Feature data
data = iris.data

print("Dataset shape:", data.shape)
print("Number of features:", data.shape[1])


# Number of clusters
k = 3

# Create K-Means model
model = KMeansCustom(n_clusters=k)

# Apply K-Means clustering
centroids, labels = model.fit(data)


# Print final centroids
print("\nFinal Centroids:")
print(centroids)


# --------------------------------------------------
# Plot the clusters
# --------------------------------------------------

colors = ['r', 'g', 'b']

for i in range(k):

    # Plot data points belonging to cluster i
    plt.scatter(
        data[labels == i, 0],
        data[labels == i, 1],
        c=colors[i],
        label=f'Cluster {i + 1}'
    )


# Plot centroids
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker='x',
    c='black',
    s=100,
    label='Centroids'
)


plt.title('K-Means Clustering on Iris Dataset')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()