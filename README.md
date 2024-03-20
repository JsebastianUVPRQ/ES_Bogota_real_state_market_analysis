# Bogotá Real State Market Analysis

## Descripción
Este proyecto se enfoca en el análisis del mercado inmobiliario en Bogotá, Colombia. Utilizando un conjunto de datos extenso sobre propiedades en venta y alquiler, 
realizamos un análisis exploratorio de datos (EDA) para identificar tendencias, patrones y anomalías en el mercado inmobiliario de Bogotá. 
Además, desarrollamos un modelo de machine learning para predecir precios de inmuebles basados en sus características. 
Finalmente, desplegamos una aplicación sencilla utilizando Streamlit para interactuar con nuestro modelo y obtener predicciones.

## Estructura del Proyecto
- `data/`: Carpeta que contiene el conjunto de datos utilizado en el análisis.
- `notebooks/`: Jupyter notebooks con el análisis exploratorio de datos (EDA) y el proceso de desarrollo del modelo.
- `src/`: Código fuente para el modelo de machine learning y utilidades adicionales.
- `app/`: Código fuente de la aplicación Streamlit.


## Configuración del Entorno
Para ejecutar este proyecto, es necesario tener Python instalado en tu sistema. Se recomienda utilizar un entorno virtual. Puedes configurar el entorno e instalar las dependencias necesarias con los siguientes comandos:

```bash
python3 -m venv venv
source venv/bin/activate  # En Windows, usa `venv\Scripts\activate`
pip install -r requirements.txt
