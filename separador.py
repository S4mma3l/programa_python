import pandas as pd
import numpy as np
from os import remove

# llamar archivos excel
archivo_uno = "My_teams2.xlsx"
archivo_dos = "New_team.xlsx"

# asignar variable a los archivos
df1 = pd.read_excel(archivo_uno)
df2 = pd.read_excel(archivo_dos)

# creacion de columnas y llamado de la informacion
orden_uno = pd.DataFrame(
    df2, columns=["Interpreter / Agent Id", "First Name", "Last Name", "PS"])

# renombrado de la informacion
Cambio_1 = orden_uno.rename(
    columns={'Interpreter / Agent Id': 'CRID', 'First Name': '1st Name'})

orden_dos = pd.DataFrame(
    df1, columns=["CRID", "1st Name", "Last Name", "PS"])


# Generacion de archivo
dataframes = [Cambio_1, orden_dos]
join = pd.concat(dataframes)
join.to_excel("temp1.xlsx")


df3 = "temp1.xlsx"
df4 = "temp1.xlsx"

df5 = pd.read_excel(df3)
df6 = pd.read_excel(df4)

df7 = pd.concat([df5, df6], axis=0)

df10 = pd.DataFrame(df7, columns=["CRID", "1st Name", "Last Name", "PS"])
df11 = df10.drop_duplicates(subset=["CRID", "1st Name", "Last Name", "PS"])

df11.to_excel("My_Team_HQ_2023.xlsx", index=False)
remove("temp1.xlsx")