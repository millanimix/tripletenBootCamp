# Estadistica_descriptiva
from matplotlib import pyplot as plt
import pandas as pd

# Histogramas de frecuencia
# data = pd.Series([11, 20, 22, 31, 32, 33, 41, 42, 43, 44, 51, 52, 53, 54, 55, 61, 62, 63, 64, 65, 66, 71, 72, 73, 74, 75, 76, 77, 81, 82, 83, 84, 85, 86, 87, 88, 91, 92, 93, 94, 95, 96, 97, 98, 99])
# data.hist(bins=4, alpha=0.5)

# data.hist(
#     bins=[11, 20, 30, 40, 50, 60, 70, 80, 90, 99], alpha=0.7
# )
# plt.show()

# Ejercicio
# el dataset pur_time (del inglés purchase_time que significa tiempo de compra)
pur_time = pd.Series([36, 44, 73, 32, 44, 29, 63, 60, 55, 74, 61, 26, 76, 40, 39, 28, 69, 61, 54, 58, 47, 41, 70, 51, 58, 36, 71, 47, 74, 59, 50, 78, 59, 48, 67, 53, 67, 52, 38, 55, 53, 53, 43, 77, 44, 63, 63, 54])
# pur_time.hist(
#     bins=[15, 30, 45, 60, 75, 90],
#     alpha=0.7
# )
pur_time.hist(
    bins=[15, 35, 55, 75, 90],
    alpha=0.5
)
pur_time.hist(
    bins=[15, 45, 55, 90],
    alpha=0.5
)

plt.show()

