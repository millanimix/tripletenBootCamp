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