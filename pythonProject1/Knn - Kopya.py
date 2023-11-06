from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import  classification_report, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
df=pd.read_csv("market.csv")
label_encoder = LabelEncoder()
df['City'] = label_encoder.fit_transform(df['City'])
df['Customer type'] = label_encoder.fit_transform(df['Customer type'])
df['Product line'] = label_encoder.fit_transform(df['Product line'])
df['Payment'] = label_encoder.fit_transform(df['Payment'])
df['cogs'] = label_encoder.fit_transform(df['cogs'])
df['Total'] = label_encoder.fit_transform(df['Total'])
df['gross income'] = label_encoder.fit_transform(df['gross income'])
df['Gender'] = label_encoder.fit_transform(df['Gender'])

print(df)
x = df[['Gender','City','Product line','gross income']] #Independent variables
y = df['Customer type']


x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.4,random_state=15)
knn = KNeighborsClassifier(n_neighbors=9)
knn.fit(x_train,y_train)
y_pred =knn.predict(x_test)


# Doğruluk oranı
accuracy: float = accuracy_score(y_test,y_pred )
print("Doğruluk Oranı:", accuracy)

