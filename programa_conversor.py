import pandas as pd

def cmAPulgadas (cm):
    return cm / 2.54

# * Leer el archivo excel

df = pd.read_excel('muebles_medidas.xlsx')

# * Añadir una columna al DataFrame que sea de pulgadas y se rellene con el cálculo  de cm / 2.54

df['Pulgadas'] = df['Centímetros'].apply(cmAPulgadas)

df.to_excel('mueble medidas convertidas.xlsx', index=False)

print ('Conversión completada y guardada en un nuevo archivo llamado \'mueble medidas convertidas.xlsx\'')