import pandas as pd
dataset = pd.read_csv('task4-1.csv')
x=dataset['YearsExperience']
y=dataset['Salary']
X=x.values.reshape(-1,1)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)
a=float(input("Enter Your Experience : "))
output = model.predict([[a]])
print(output)
