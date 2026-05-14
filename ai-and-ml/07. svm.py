import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

df = pd.read_excel('data.xlsx')

X = df[['Feature1', 'Feature2']]
y = df['Class']

label_encoder = LabelEncoder()

y_encoded = label_encoder.fit_transform(y)

model = SVC(kernel='linear')

model.fit(X, y_encoded)

w = model.coef_[0]

margin = 2 / np.linalg.norm(w)

print(f"Maximum margin: {margin:.4f}")

plt.scatter(
    X.iloc[:, 0],
    X.iloc[:, 1],
    c=y_encoded,
    cmap='coolwarm',
    marker='o'
)

b = model.intercept_[0]

x_vals = np.linspace(
    X.iloc[:, 0].min(),
    X.iloc[:, 0].max(),
    100
)

y_vals = -(w[0] * x_vals + b) / w[1]

plt.plot(
    x_vals,
    y_vals,
    'k--',
    label='Decision Boundary'
)

support_vectors = model.support_vectors_

plt.scatter(
    support_vectors[:, 0],
    support_vectors[:, 1],
    facecolors='none',
    edgecolors='red',
    s=100,
    label="Support Vectors"
)

plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

plt.title('SVM Decision Boundary with Support Vectors')

plt.legend()
plt.grid(True)
plt.show()
