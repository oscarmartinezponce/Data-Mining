from models.table import Table
from models.algorithms.kmeans import KMeans

header = {"var1": Table._numeric, "var2": Table._numeric, "var3": Table._numeric,
          "var4": Table._numeric, "var5": Table._numeric, "class": Table._nominal}
data = [
    [7,	8,	4,	5,	2, ''], [6,	8,	5,	4,	2, ''], [8,	9,	7,	8,	9, ''],
    [6,	7,	7,	7,	8, ''], [1,	2,	5,	3,	4, ''], [3,	4,	5,	3,	5, ''],
    [7,	8,	8,	6,	6, ''], [8,	9,	6,	5,	5, ''], [2,	3,	5,	6,	5, ''],
    [1,	2,	4,	4,	2, ''], [3,	2,	6,	5,	7, ''], [2,	5,	6,	8,	9, ''],
    [3,	5,	4,	6,	3, ''], [3,	5,	5,	6,	3, '']]

table = Table(data, header, 5) # Crea una tabla, el 3 parámetro indica el indice de la clase

means = KMeans(table, 2, 3, 20, 20) # (min_k, max_k, i, r)
means.run()
print("Error: " + str(means.error))
print("Asignación de los clusters " + str(means.clusters)) # Esta es la columna que le interesa al maestro
print("Datos y asignación de los clusters")
print(means) # Imprime los datos y el cluster al que fue asignado
print("Centroides:" + str(means.centroids))
