import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder

# SVM modelini oluşturun
df =pd.read_csv("obesity.csv")

le = LabelEncoder()
df['Label'] = le.fit_transform(df['Label'])
X = df[["Age","Height","Weight","BMI"]]  # Bağımsız değişkenler
y = df['Label']
# Bağımlı değişken
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=21)
# SVM modelini oluşturun
model = SVC(kernel='poly')  # Doğrusal SVM
# Modeli eğitin
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Doğruluk oranını hesaplayın
accuracy = accuracy_score(y_test, y_pred)
print("Doğruluk Oranı:", accuracy)
print(y_test)
print(y_pred)