import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('C:\\Users\\Sunny\\linear_regression_0419.csv')
df

X = df.iloc[:,:-1].values
Y = df.iloc[:,:-1].values

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X,Y)

y_pred = reg.predict(X)
y_pred

plt.scatter(X, Y, color='blue')
plt.plot(X, y_pred, color='green')
plt.title('Weight')
plt.xlabel('cm')
plt.ylabel('kg')
plt.show()
