# vamos a construir un modelo con scikit learn
# para predecir la columna Valor_m2_Barrio
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


# cargamos el dataset
df = pd.read_csv('property_census_loaded_bogota.csv')

