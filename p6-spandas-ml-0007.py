import pandas as pd
import numpy as np
# Alexandro Aguilar NC 0007
serie_amigos = ["Caleb", "Meredith", "Lia", "Yahir", "Abril", "Darrell", "Daniel"]
print("--- Serie listado de amigos NC 0007 ---")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes = [20, 50, 100, 200, 500, 1000]
print("--- Serie listado valor de billetes NC 0007 ---")
billetes=pd.Series(serie_billetes)
print(billetes)

serie_billetes = [20, 50, 100, 200, 500, 1000]
serie_bletras = ["veinte", "cincuenta", "cien", "Doscientos", "Quinientos", "Mil"]
print("--- Serie listado nombre y valor de billetes MX NC 0007 ---")
tablabilletes=pd.Series(serie_billetes, serie_bletras)
print(tablabilletes)

# Diccionario dataframe
# Diccionario de valor monedas y nombre
print("Datos de diccionario a DataFrame en pandas")
dic_monedas = {
    "serie_billetes": [20, 50, 100, 200, 500, 1000],
    "serie_bletras": ["veinte", "cincuenta", "cien", "Doscientos", "Quinientos", "Mil"]
} 
tablabillete = pd.DataFrame(dic_monedas, index=["A", "B", "C", "D", "E", "F"])
print(tablabillete)

print("Casa de cambio de Alexandro Aguilar NC 0007")
