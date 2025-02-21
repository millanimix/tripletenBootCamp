# DADS_S7W1C1 ---------------------------------------- 
# Ejercicio 1 ---------------------------------------- 

mkdir proyecto_x
cd proyecto_x
ls -a
touch logs.txt
mkdir scripts textos
ls -a 

# Ejercicio 2 ---------------------------------------- 

echo "ESTE ES UN REGISTRO DE ACTIVIDADES
==================================
Autor: [Su nombre]
Fecha: [Fecha de hoy]

Resultados:
" > logs.txt

cat logs.txt
wc -m logs.txt
mv logs.txt ./textos

date +"%H:%M Creacion de Log" >> textos/logs.txt

alias conteo_caracteres="wc -m"
conteo_caracteres textos/logs.txt

# DADS_S7W1C2 ---------------------------------------- 
# Ejercicio 1 ---------------------------------------- 

logger(){
    date +"%H:%M Creacion de $1" >> textos/logs.txt
}

echo "
for i in range(1,11,1): 
    if i%2 == 0:
        print(i)
" > scripts/pares.py

logger pares.py
python scripts/pares.py

# Ejercicio 2 ---------------------------------------- 

echo "
import numpy as np 
import pandas as pd 

n = 100 
media = 5 
desv = 2 

datos = np.random.normal(size = n, loc = media, scale = desv) 
datos = datos.round(0).astype(int) 

datos_trim = [] 
for i in range(len(datos)): 
  if datos[i] <= abs(media) + 2*desv or datos[i] >= abs(media) - 2*desv: 
    datos_trim.append(datos[i]) 

datos_trim = pd.DataFrame(datos_trim) 
datos_trim.columns = ['Datos'] 
histograma = datos_trim.groupby('Datos').size() 

for i in range(len(histograma)): 
  if histograma.index[i]>=0: 
    s = \"+\" 
  else: 
    s = \"\" 
  print( 
    s, 
    histograma.index[i], 
    ' '*(1+len(str(np.max([np.max(histograma.index), 
                           abs(np.min(histograma.index))]))) - 
                           len(str(abs(histograma.index[i])))), 
    '*'*round(100*histograma.iloc[i]/len(datos_trim)), 
    sep = \"\" 
    )
" > scripts/histograma.py

logger histograma.py
python scripts/histograma.py


