# vamos a construir un modelo con scikit learn
# para predecir la columna Valor_m2_Barrio
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# cargamos el dataset
df = pd.read_csv('property_census_loaded_bogota.csv')
# eliminamos valores nulos
df = df.dropna()

# seleccionamos las columnas que vamos a usar para el modelo
X = df[['Habitaciones', 'Baños', 'Área', 'valor_m2']]

y = df['valor']
# dividimos el dataset en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# creamos el modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)

# entrenamos el modelo
model.fit(X_train, y_train)

# usamos streamlit para guardar el modelo
import joblib
joblib.dump(model, 'random_forest_bogota.pkl')
