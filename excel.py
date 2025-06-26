import pandas as pd

# 1️⃣ Carga del archivo Excel
# Asegúrate de poner la ruta correcta si es necesario
df = pd.read_excel(r"C:\Users\USER\OneDrive\Escritorio\EJERCICIO PYTHON\precio_oro_1900_2025.xlsx")

# 2️⃣ Muestra las primeras 5 filas para verificar
print(df.head())

# 3️⃣ Crear columna de relación Precio_Oro / PIB_Per_Capita
df["Ratio_Oro_PIB"] = df["Precio_Oro_USD"] / df["PIB_Per_Capita_USD"]

# 4️⃣ Encuentra la fila donde esta razón es máxima
fila_max = df.loc[df["Ratio_Oro_PIB"].idxmax()]

# 5️⃣ Imprimir los resultados
print("\nAño donde el oro tuvo el mayor valor en relación al PIB per cápita:")
print(f"Año: {fila_max['Año']}")
print(f"Precio del oro: ${fila_max['Precio_Oro_USD']}")
print(f"PIB per cápita: ${fila_max['PIB_Per_Capita_USD']}")
print(f"Ratio Oro/PIB: {fila_max['Ratio_Oro_PIB']:.4f}")

