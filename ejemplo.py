from sklearn.linear_model import LinearRegression
import numpy as np

# Datos
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

#modelo
modelo = LinearRegression()

#entrenar
modelo.fit(X, y)

#predecir
pred = modelo.predict([[5]])

print(pred)