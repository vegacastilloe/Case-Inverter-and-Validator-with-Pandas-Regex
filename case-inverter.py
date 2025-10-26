import pandas as pd
import re
from tabulate import tabulate
# 📦 Leer y limpiar el archivo
df_raw = pd.read_excel(url, header=0).dropna(axis=1, how='all')
df_raw.columns = df_raw.columns.str.strip()
df_input = df_raw.iloc[:, :1]

# 🧠 Funcion para convertir texto 
def convert_case(texto):
 return re.sub(r'(\b[a-z]+\b)|(\b[A-Z]+\b)', lambda m: m.group()
 .lower() if m.group()
 .isupper() else m.group().upper(), texto)

# 🚀 Aplicar al DataFrame
df_input['My Answer'] = df_input['Question'].apply(convert_case)
df_input['Answer Given'] = df_raw.iloc[:, 1:]
df_input['Match'] = df_input['Answer Given'] == df_input['My Answer']
print(tabulate(df_input.values, df_input.columns, tablefmt='psql'))

# 💾 Exportación opcional
# df_input.to_excel("case-inverter_output.xlsx", index=False)