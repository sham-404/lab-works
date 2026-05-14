import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder

df = pd.read_excel("weather_data.xlsx")

label_encoders = {}

for column in df.columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

X = df[['Outlook', 'Temperature', 'Humidity', 'Windy']]
y = df['Play']

model = CategoricalNB()
model.fit(X, y)

test_instance = [
    label_encoders['Outlook'].transform(['Rainy'])[0],
    label_encoders['Temperature'].transform(['Cool'])[0],
    label_encoders['Humidity'].transform(['High'])[0],
    label_encoders['Windy'].transform([True])[0]
]

predicted = model.predict([test_instance])

predicted_label = label_encoders['Play'].inverse_transform(predicted)

print("Predicted outcome for 'Play':", predicted_label[0])
