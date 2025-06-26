import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Leer el archivo Excel
df = pd.read_excel("precio_oro_1900_2025.xlsx")

# 2️⃣ Crear una nueva columna para la relación Precio_Oro / PIB_per_Capita
df["Relacion_Oro_PIB"] = df["Precio_Oro_USD"] / df["PIB_Per_Capita_USD"]

# 3️⃣ Identificar el año donde esta relación es máxima
año_max = df.loc[df["Relacion_Oro_PIB"].idxmax(), "Año"]
max_relacion = df["Relacion_Oro_PIB"].max()

# 4️⃣ Imprimir resultado
print(f"Año en que el oro tuvo el mayor valor en relación al PIB per cápita: {año_max}")
print(f"Relación Precio_Oro / PIB_per_Cápita: {max_relacion:.4f}")

# 5️⃣ Crear la gráfica
plt.figure(figsize=(12, 6))
plt.plot(df["Año"], df["Relacion_Oro_PIB"], label="Relación Precio_Oro / PIB_per_Cápita", color="blue", marker="o")
plt.scatter(año_max, max_relacion, color="red", zorder=5, label=f"Año máximo ({año_max})")
plt.title("Relación Precio del Oro vs PIB per Cápita (1900–2025)", fontsize=14)
plt.xlabel("Año", fontsize=12)
plt.ylabel("Relación Precio_Oro / PIB_per_Cápita", fontsize=12)
plt.legend()
plt.grid(True)

# 6️⃣ Guardar la gráfica como imagen
plt.savefig("grafica_oro_vs_pib.png")

# 7️⃣ Mostrarl
plt.show()
