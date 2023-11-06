#Kullanılacak kütüphanelerin içe aktarımı

from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,r2_score
#Kullanılacak Verinin içe aktarımı

df=pd.read_csv("advertising.csv")
x = df[['TV Ad Budget ($)','Radio Ad Budget ($)','Newspaper Ad Budget ($)']] #Independent variables
y = df['Sales ($)']
#Algoritmanın yüklenmesi ve eğitimi

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=15)
lr = LinearRegression()
lr.fit(x_train,y_train)
y_pred =lr.predict(x_test)
#Metriklerin belirtilmesi ve sonuçlar

coefficients = lr.coef_
intercept = lr.intercept_
mse = mean_squared_error(y_test,y_pred)
r_2 =r2_score(y_test,y_pred)
print("R2:", r_2)
print("mse:", mse)
print("coefficients:", coefficients)
print("intercept:", intercept)
