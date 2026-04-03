import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def preparar_datos_para_clustering(df, columnas_multi):
    """
    Transforma columnas de texto (selección múltiple) en una matriz numérica (0 y 1).
    """
    df_modelo = df.copy()

    for col in columnas_multi:
        # Usamos el separador avanzado que descubrimos en el EDA
        series_explodida = df_modelo[col].str.get_dummies(sep=', ')
        #Añadimos el nombre de la columna origonal para no confundir 'Cine' de intereses con otro
        series_explodida.columns = [f"{col}_{c.strip()}" for c in series_explodida.columns]
        df_modelo = pd.concat([df_modelo, series_explodida], axis=1)
    
    # Nos quedamos solo con las columnas numéricas para la IA
    # Seleccionamos solo las que acabamos de crear y "edad" o "conexion"
    cols_numericas = df_modelo.select_dtypes(include=["int64", "float64", "uint8"]).columns
    return df_modelo[cols_numericas].fillna(0)

def aplicar_kmeans(data, n_clusters=3):
    """
    Entrena el modelo K-Means y devuelve las etiquetas de los grupos.
    """
    # Escalamos los datos (importante para que la edad no pese más que un 0/1)
    scaler= StandardScaler()
    data_scaled = scaler.fit_transform(data)

    # Creamos y entrenamos el modelo
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    clusters = model.fit_predict(data_scaled)

    return clusters, model