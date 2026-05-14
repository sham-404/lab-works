import pandas as pd

from sklearn.ensemble import RandomForestClassifier, VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('heart.csv')

X = df.drop('target', axis=1)
y = df['target']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

dt = DecisionTreeClassifier()
rf = RandomForestClassifier()
svm = SVC(probability=True)

dt.fit(X_train, y_train)
rf.fit(X_train, y_train)
svm.fit(X_train, y_train)

dt_pred = dt.predict(X_test)
rf_pred = rf.predict(X_test)
svm_pred = svm.predict(X_test)

voting_clf = VotingClassifier(
    estimators=[
        ('dt', dt),
        ('rf', rf),
        ('svm', svm)
    ],
    voting='hard'
)

voting_clf.fit(X_train, y_train)

ensemble_pred = voting_clf.predict(X_test)

def convert_to_yes_no(predictions):
    return [
        'Yes' if p == 1 else 'No'
        for p in predictions
    ]

dt_results = convert_to_yes_no(dt_pred)
rf_results = convert_to_yes_no(rf_pred)
svm_results = convert_to_yes_no(svm_pred)
ensemble_results = convert_to_yes_no(ensemble_pred)

LIMIT = 5

print("Decision Tree Predictions:")

for i, result in enumerate(dt_results[:LIMIT], 1):
    print(f"Patient {i}: {result}")

print("\nRandom Forest Predictions:")

for i, result in enumerate(rf_results[:LIMIT], 1):
    print(f"Patient {i}: {result}")

print("\nSVM Predictions:")

for i, result in enumerate(svm_results[:LIMIT], 1):
    print(f"Patient {i}: {result}")

print("\nVoting Ensemble Predictions:")

for i, result in enumerate(ensemble_results[:LIMIT], 1):
    print(f"Patient {i}: {result}")
