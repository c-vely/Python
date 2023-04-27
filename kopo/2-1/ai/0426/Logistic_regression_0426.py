
# 데이터 불러오기
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
    
df = pd.read_csv('C:\\Users\\Sunny\\Logistic_regression_example.csv', encoding='cp949')
df 

X = df.iloc[:,:-1].values
Y = df.iloc[:,-1].values


# 학습
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, Y_train)

classifier.predict([[3300]])
classifier.predict([[2100]])

classifier.predict_proba([[3300]])
classifier.predict_proba([[2100]])


# 테스트 > 예측 > 평가
X_test
Y_test
Y_pred = classifier.predict(X_test)
Y_pred
classifier.score(X_test, Y_test)


X_range = np.arange(min(X), max(X), 10)
X_range
S = 1 / (1 + np.exp(-(classifier.coef_ * X_range + classifier.intercept_)))
S
S.shape
X_range.shape
S = S.reshape(-1)
S.shape


# train데이터 시각화
plt.scatter(X_train, Y_train, color = 'blue')
plt.plot(X_range, S, color='green')
plt.plot(X_range, np.full(len(X_range), 0.5), color='red')
plt.title('Monthly pay')
plt.xlabel('annual income')
plt.ylabel('S')
plt.show()


# test데이터 시각화
plt.scatter(X_test, Y_test, color = 'blue')
plt.plot(X_range, S, color='green')
plt.plot(X_range, np.full(len(X_range), 0.5), color='red')
plt.title('Monthly pay')
plt.xlabel('annual income')
plt.ylabel('S')
plt.show()


# 혼동 행렬
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
cm

