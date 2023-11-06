from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
df=pd.read_csv("market.csv")
label_encoder = LabelEncoder()
df['Payment'] = label_encoder.fit_transform(df['Payment'])
df['Gender'] = label_encoder.fit_transform(df['Gender'])
df['Product line'] = label_encoder.fit_transform(df['Product line'])
print(df)
x = df[['Gender','Product line','Payment']] #Independent variables
y = df['gross income']
std = StandardScaler()
scaler_x=std.fit_transform(x)
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=15)
lr = LinearRegression()
lr.fit(x_train,y_train)
y_pred =lr.predict(x_test)
coefficients = lr.coef_
intercept = lr.intercept_
mse = mean_squared_error(y_test,y_pred)
r_2 =r2_score(y_test,y_pred)
print("R2:", r_2)
print("mse:", mse)
print("coefficients:", coefficients)
print("intercept:", intercept)


