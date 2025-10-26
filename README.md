# 🔄 Case Inverter & Validator with Pandas + Regex

![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![Last Updated](https://img.shields.io/github/last-commit/vegacastilloe/Case-Inverter-and-Validator-with-Pandas-Regex)
![Language](https://img.shields.io/badge/language-español-darkred)

#
---
- 🌟 Every Other Day Excel and Power Query Challenges No316 🌟
- 🌟 **Author**: Omid Motamedisedeh

    - 🔰 In the question table, convert lowercase characters to uppercase and vice versa.

 🔰 Este script transforma palabras en una columna de texto invirtiendo su capitalización (mayúsculas ↔ minúsculas) y compara el resultado con una respuesta esperada. Ideal para validaciones automáticas en formularios, tests o flujos de NLP.

 🔗 Link to Excel file:
 👉 https://lnkd.in/gfssqbWY

**My code in Python** 🐍 **for this challenge**

 🔗 https://github.com/vegacastilloe/Case-Inverter-and-Validator-with-Pandas-Regex/blob/main/case-inverter.py

---
---

## Case Inverter & Validator with Pandas + Regex

Este script transforma palabras en una columna de texto invirtiendo su capitalización (mayúsculas ↔ minúsculas) y compara el resultado con una respuesta esperada.



## 📦 Requisitos

- Python 3.9+
- Paquetes:
- pandas openpyxl (para leer .xlsx)
- tabulate (solo para impresión bonita)
- Archivo Excel con al menos:
    - La columna: `Question`.
    - En la columna `Result` : resultados esperados para comparación

---

## 🚀 Cómo funciona

- Lee un archivo Excel desde una URL o ruta local.
- Limpia columnas vacías y espacios en los encabezados.
- Aplica una transformación regex para invertir el case de palabras completas.
- Compara el resultado con una columna de respuestas.
- Imprime una tabla con el resultado y la validación.

---

## 📤 Salida

El script imprime un DataFrame con:

1. `Question`
2. `My Answer`
3. `Answer Given`
4. `Match`

---

## 🧹 Output:


|Question|My Answer|Answer Given|Match|
|--------|--------|--------|--------|
|apple|APPLE|APPLE|True|
|BANANA|banana|banana|True|
|Cherry|Cherry|Cherry|True|
|daTE|daTE|daTE|True|
|elderberry|ELDERBERRY|ELDERBERRY|True|

---

## 🛠️ Personalización

Puedes adaptar el script para:

- Aplicar reglas más complejas
- Exportar el resultado a Excel o CSV

---

## 🚀 Ejecución

```python
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
```

### 💾 Exportación opcional
```python
# df_input.to_excel("case-inverter_output.xlsx", index=False)
```
---
### 📄 Licencia
---
Este proyecto está bajo ![License: MIT](https://img.shields.io/badge/License-MIT-cyan.svg). Puedes usarlo, modificarlo y distribuirlo libremente.

---
