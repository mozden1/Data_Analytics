from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
df = pd.read_csv("market.csv")
le = LabelEncoder()
df['Gender'] = le.fit_transform(df['Gender'])
df['Product line'] = le.fit_transform(df['Product line'])

X = df[["Product line","gross income"]]  # Bağımsız değişkenler
y = df['Gender']  # Bağımlı değişken
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=15)

model = RandomForestClassifier(n_estimators=100, random_state=42)

# Modeli eğitin
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))

# Karışıklık matrisi
print(confusion_matrix(y_test, y_pred))

# Doğruluk oranı
accuracy = accuracy_score(y_test, y_pred)
print("Doğruluk Oranı:", accuracy)