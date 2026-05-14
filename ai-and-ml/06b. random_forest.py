import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

df = pd.read_excel('fruit_data.xlsx')

df['Fruit_Type_Label'] = df['Fruit Type'].map({
    'Apple': 0,
    'Orange': 1,
    'Banana': 2
})

X = df[['Weight (g)', 'Color (encoded)', 'Size (cm)', 'Shape (encoded)']]
y = df['Fruit_Type_Label']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

y_pred = rf_model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy * 100:.2f}%')

def predict_fruit(weight, color, size, shape):
    prediction = rf_model.predict([[weight, color, size, shape]])

    fruit_types = {
        0: 'Apple',
        1: 'Orange',
        2: 'Banana'
    }

    print(
        f'The predicted fruit is: {fruit_types[prediction[0]]}'
    )

predict_fruit(160, 1, 6, 1)
