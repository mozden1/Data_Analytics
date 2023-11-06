import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
df =pd.read_csv("happy.csv")
X = df[["infoavail","housecost","schoolquality","policetrust","streetquality","ëvents"]]  # Bağımsız değişkenler
y = df['happy']                # Bağımlı değişken
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=15)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Sınıflandırma raporu
print(classification_report(y_test, y_pred))

# Karışıklık matrisi
print(confusion_matrix(y_test, y_pred))

# Doğruluk oranı
accuracy: float = accuracy_score(y_test, y_pred)
print("Doğruluk Oranı:", accuracy)

print(y_pred)
y_pred = y_pred.squeeze()
x_test_view = X_test['ëvents'].values.squeeze()
sns.scatterplot(x = x_test_view, y = y_pred, hue = y_test)
plt.xlabel('Radius')
plt.ylabel('Predicted')
plt.legend()