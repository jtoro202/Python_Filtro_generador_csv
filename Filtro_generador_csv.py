import pandas as pd

# Ruta donde se encuentra el archivo a leer, reemplazar la ruta que se encuentra dentro de las comillas.
rutadrive = "\\REPOSITORIO\\Filtro\\censo_viviendas.csv"

# Lectura del archivo como dataframe el cual se encuentra separado por "|", reemplazar por la separacion que posee el archivo csv.
print("Leyendo Archivo ..........")
datos = pd.read_csv(rutadrive, sep = '|', low_memory = False)

# Ciclo donde realizamos la busqueda, en este caso los departamentos a separar en archivos independientes, ["nombre_departamento"].
# Reemplazar lo que se encuntra entre comillas por la cabezera y la ruta a guardar.
departamentos = datos["nombre_departamento"].unique()
i = 0
for departamento in departamentos:
  datosDepartamentos = datos[datos["nombre_departamento"] == departamento]
  rutadeguardado = "\\REPOSITORIO\\Filtro\\DatasetFiltrado\\" + departamento.strip() + ".csv"
  datosDepartamentos.to_csv(rutadeguardado, index = False)
  i += 1
  print(f"Se guardo el departamento de: {departamento}")
print("Total de Departamentos: " + str(i))