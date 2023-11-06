import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import graphviz

df = pd.read_csv("obesity.csv")
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])

X = df[["ID", "Age", "Gender", "Height", "Weight", "BMI"]]  # Bağımsız değişkenler
y = df['Label']  # Bağımlı değişken

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Karar Ağacı modelini oluşturun
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Doğruluk oranını hesaplayın
accuracy = accuracy_score(y_test, y_pred)
print("Doğruluk Oranı:", accuracy)


