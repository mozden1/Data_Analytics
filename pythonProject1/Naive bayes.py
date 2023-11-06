import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
df =pd.read_csv("diabet.csv")
documents = df[["glucose","bloodpressure"]]
labels=df["diabetes"]
X_test: object
X_train, X_test, y_train, y_test = train_test_split(documents, labels, test_size=0.2, random_state=42)

clf = MultinomialNB()

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
confusion = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:")
print(confusion)
print("Classification Report:")
print(classification_rep)

