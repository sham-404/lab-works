import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans

df = pd.read_excel(
    'student_marks.xlsx',
    header=1
)

print("Dataset:")
print(df)

X = df[['Maths', 'Science']]

kmeans = KMeans(
    n_clusters=2,
    random_state=0
)

kmeans_labels = kmeans.fit_predict(X)

df['Cluster'] = kmeans_labels

plt.figure(figsize=(8, 6))

plt.scatter(
    df[df['Cluster'] == 0]['Maths'],
    df[df['Cluster'] == 0]['Science'],
    s=100,
    c='blue',
    label='Cluster 0'
)

plt.scatter(
    df[df['Cluster'] == 1]['Maths'],
    df[df['Cluster'] == 1]['Science'],
    s=100,
    c='red',
    label='Cluster 1'
)

centroids = kmeans.cluster_centers_

plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    s=200,
    c='red',
    marker='X',
    label='Centroids'
)

plt.xlabel('Maths Marks')
plt.ylabel('Science Marks')

plt.title('Student Clusters Based on Marks')

plt.legend()
plt.grid(True)
plt.show()

print("\nCluster Results for Each Student:")
print(df)
